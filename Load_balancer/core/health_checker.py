import threading
import time
import requests
from typing import List
from backend.backend_server import BackendServer

class HealthChecker:
    def __init__(self, servers: List[BackendServer], health_check_path: str ="/") -> None:
        """
        Initialize the HealthChecker.
        
        :param servers: List of server URLs to monitor.
        :param health_check_path: Endpoint path for health checks.
        """
        self.servers = servers
        self.health_check_path = health_check_path
        self.running = False
        self.thread = None
    
    def start(self, interval: int) -> None:
        """
        Start periodic health checks in a background thread.
        
        :param interval: Time in seconds between health checks.
        """
        if self.running:
            print("Health checker is already running.")
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._run_health_checks, args=(interval,))
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self) -> None:
        """Stop the health checks."""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()
        print("Health check stopped.")
    
    def _run_health_checks(self, interval: int) -> None:
        """"Perform periodic health checks."""
        while self.running:
            self._perform_health_checks()
            time.sleep(interval)
    
    def _perform_health_checks(self) -> None:
        """Check the health of all servers and update their status."""
        for server in self.servers:
            is_healty = self._check_server_health(server)
            server.update_health_status(is_healty)
    
    def _check_server_health(self, server: BackendServer) -> bool:
        """
        Check the health of a single server.
        
        :param server: Server URL to check.
        :return: True if the server is healthy, False otherwise.
        """

        try:
            url = f"http://{server.host}:{server.port}{self.health_check_path}"
            response = requests.get(url, timeout=2)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Health check failed for {server.host}:{server.port} - {e}")
            return False
    
    def get_active_servers(self) -> List[BackendServer]:
        """
        Retrieve the list of servers that are currently healthy.
        
        :return: List of healthy servers.
        """
        return [server for server in self.servers if server.is_alive]