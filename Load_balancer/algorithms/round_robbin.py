from .base import LoadBalancingAlgorithm
from typing import List
from backend.backend_server import BackendServer

class RoundRobinAlgorithm(LoadBalancingAlgorithm):
    """Round-robbin algorithm for load balancing."""
    
    def __init__(self) -> None:
        self._last_server_index = 0

    def get_next_server(self, active_servers: List[BackendServer]) -> BackendServer:
        """Get the next server to serve a request.

        Args:
            active_servers (list): List of active servers.

        Returns:
            Server: The next server to serve a request.
        """
        if not active_servers:
            return None

        server = active_servers[self._last_server_index]
        self._last_server_index = (self._last_server_index + 1) % len(active_servers)
        return server