import json
from backend.backend_server import BackendServer
from typing import List

def load_servers(config_file: str) -> List[BackendServer]:
    """
    Load servers from a JSON configuration file and create BackendServer instances.

    :param config_file: Path to the JSON configuration file.
    :return: List of BackendServer instances.
    """
    try:
        with open(config_file, "r") as file:
            server_configs = json.load(file)
        
        servers = []
        for config in server_configs:
            server = BackendServer(id=config["id"], host=config["host"], port=config["port"])
            servers.append(server)
        
        return servers
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_file}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Configuration file '{config_file}' is not a valid JSON file.")
        return []