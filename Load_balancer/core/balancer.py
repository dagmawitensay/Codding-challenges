import socket
from threading import Thread
from algorithms.round_robbin import RoundRobinAlgorithm
from .health_checker import HealthChecker
from backend.backend_server import BackendServer
from .config import HEALTH_CHECK_INTERVAL

class LoadBalancer:
    def __init__(self, health_checker: HealthChecker, host: str ="localhost", port: int =80, algorithm: str ="round_robin"):
        self.servers = []
        self._algorithm = self._select_algorithm(algorithm)
        self.host = host
        self.port = port
        self.health_checker = health_checker
        self.health_check_interval = HEALTH_CHECK_INTERVAL
        self.running = False
    
    def _select_algorithm(self, algorithm: str) -> object:
        if algorithm == "round_robin":
            return RoundRobinAlgorithm()
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

    def get_next_server(self) -> BackendServer:
        active_servers = self.health_checker.get_active_servers()
        return self._algorithm.get_next_server(active_servers)

    def _handle_request(self, client_conn: socket.socket) -> None:
        server = self.get_next_server()
        print(f"Selected server: {server.host}:{server.port}")
        if not server:
            response = "HTTP/1.1 503 Service Unavailable\r\n\r\nNo active servers!"
            client_conn.sendall(response.encode())
            client_conn.close()
            return
        
        try:
            server.handle_connections(client_conn)
        except Exception as e:
            print(f"Error handling request: {e}")
        finally:
            client_conn.close()
    
    def start(self) -> None:
        def handle_client(client_conn, client_addr):
            self._handle_request(client_conn)
        
        self.start_health_check()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lb_socket:
            lb_socket.bind((self.host, self.port))
            lb_socket.listen(5)
            lb_socket.settimeout(1.0)
            print(f"Load balancer running on port {self.port}")

            self.running = True
            try:
                while self.running:
                    try:
                        client_conn, client_addr = lb_socket.accept()
                        Thread(target=handle_client, args=(client_conn, client_addr)).start()
                    except socket.timeout:
                        pass
            except KeyboardInterrupt:
                print("\nShutting down Load Balancer...")
            finally:
                self.running = False
                lb_socket.close()
                self.stop_health_check()  
                print("Load balancer stopped.")
    
    def start_health_check(self) -> None:
        """
        Start periodic health checks for all servers.
        """
        self.health_checker.start(self.health_check_interval)

    def stop_health_check(self) -> None:
        """
        Stop periodic health checks.
        """
        self.health_checker.stop()