#!/usr/bin/env python
import argparse
from core.balancer import LoadBalancer
from core.health_checker import HealthChecker
from servers.server import load_servers


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Load Balancer Command Line Tool")
    parser.add_argument("--host", type=str, default="localhost", help="Host address for the load balancer (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=80, help="Port for the load balancer (default: 8000)")
    parser.add_argument("--interval", type=int, default=5, help="Health check interval in seconds (default: 5)")
    parser.add_argument("--config", type=str, default="servers/servers.json", help="Path to the server configuration file")
    
    args = parser.parse_args()

    # Load server configurations
    backend_servers = load_servers(args.config)
    if not backend_servers:
        print(f"No servers found in the configuration file: {args.config}")
        return

    health_checker = HealthChecker(backend_servers)
    load_balancer = LoadBalancer(
        health_checker=health_checker,
        port=args.port,
        algorithm="round_robin",
    )
    load_balancer.servers = backend_servers
    health_checker.health_check_interval = args.interval 

    try:
        print(f"Starting Load Balancer on {args.host}:{args.port} with health check interval {args.interval}s...")
        load_balancer.start()
    except KeyboardInterrupt:
        print("\nStopping Load Balancer...")
    finally:
        print("Stopping Health Checker...")
        health_checker.stop()


if __name__ == "__main__":
    main()
