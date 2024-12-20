from abc import ABC, abstractmethod

class LoadBalancingAlgorithm(ABC):
    """Abstract class for load balancing algorithms."""

    @abstractmethod
    def get_next_server(self, active_servers: list):
        """Get the next server to serve a request.

        Args:
            active_servers (list): List of active servers.

        Returns:
            Server: The next server to serve a request.
        """
        pass