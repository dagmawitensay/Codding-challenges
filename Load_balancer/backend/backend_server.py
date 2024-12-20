import socket
import threading


class BackendServer:
    def __init__(self, id: int, host: str, port: int) -> None:
        self.id = id
        self.host = host
        self.port = port
        self.is_alive = True
        self.lock = threading.Lock()
        self.num_connections = 0
    
    def connect(self) -> None:
        self.backend_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.backend_conn.connect((self.host, self.port))
    
    def update_health_status(self, is_alive: bool) -> None:
        with self.lock:
            self.is_alive = is_alive
    
    def handle_connections(self, client_conn: socket.socket) -> None:
        def forward_request(source: socket.socket, destination: socket.socket, log: bool = False) -> None:
            with self.lock:
                self.num_connections += 1
            
            try:
                while True:
                    data = source.recv(1024)
                    if len(data) == 0:
                        break
                        
                    if log:
                        print(f"Received request from {source.getpeername()[0]}")
                        print(data.decode("utf-8", errors="ignore"))

                    destination.send(data)
            except Exception as e:
                 print(f"Connection error: {e}")
            finally:
                with self.lock:
                    self.num_connections -= 1
        
        if not self.is_alive:
            return
        
        self.connect()
        client2backend_thread = threading.Thread(target=forward_request, args=(client_conn, self.backend_conn, True))
        backend2client_thread = threading.Thread(target=forward_request, args=(self.backend_conn, client_conn))
        client2backend_thread.start()
        backend2client_thread.start()
        client2backend_thread.join()
        backend2client_thread.join()
        client_conn.close()
        self.backend_conn.close()

    
