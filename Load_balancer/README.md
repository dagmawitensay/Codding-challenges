# Load Balancer Implementation

This project implements a robust Load Balancer to distribute HTTP requests among multiple backend servers, ensuring reliability, scalability, and high availability. It uses multithreading for efficient concurrent operations and includes features like dynamic server health checks and fault tolerance.

---

## Features

### Core Functionalities

1. **Load Balancing**:
   - Distributes requests to backend servers using the Round Robin algorithm.
   - Ensures fair distribution of traffic across healthy servers.

2. **Health Checks**:
   - Periodically pings backend servers to monitor their `/` endpoints.
   - Excludes unhealthy servers from the pool and reintegrates them upon recovery.

3. **Threaded Communication**:
   - Handles bidirectional communication between clients and backend servers using multithreading.
   - Ensures smooth concurrent processing of multiple client connections.

4. **CLI Tool**:
   - Accepts runtime configurations for host, port, health check intervals, and server configuration files.
   - Provides flexibility in deployment and testing environments.

5. **Graceful Shutdown**:
   - Cleans up resources and stops background threads on `Ctrl+C`.

---

## How It Works

### High-Level Workflow

1. **Server Registration**:
   Backend servers are registered through a JSON configuration file with details like `host`, `port`, and `id`.

2. **Health Monitoring**:
   A periodic health check ensures only active servers receive requests. Servers are marked as:
   - `healthy` if they respond successfully.
   - `unhealthy` if they fail multiple health checks.

3. **Request Handling**:
   - The load balancer listens for incoming requests.
   - Each request is routed to a healthy backend server based on Round Robin logic.

4. **Concurrency**:
   - Each client-server connection is handled by two threads:
     - Client-to-server communication.
     - Server-to-client communication.

5. **Dynamic Reconfiguration**:
   - Automatically detects server failures and recovers when servers become healthy again.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Install required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

---

## Usage

### Starting the Load Balancer

1. Configure the backend servers in `servers/servers.json`:
   ```json
   [
     {"id": 1, "host": "127.0.0.1", "port": 8001},
     {"id": 2, "host": "127.0.0.1", "port": 8002},
     {"id": 3, "host": "127.0.0.1", "port": 8003}
   ]
   ```

2. Run the load balancer:
   ```bash
   ./lb --host 127.0.0.1 --port 8000 --interval 10 --config servers/servers.json
   ```

### Sending Requests

Send HTTP requests to the load balancer:
```bash
curl http://127.0.0.1:8000
```

### Customizable CLI Options

- `--host`: Load balancer host (default: `127.0.0.1`).
- `--port`: Load balancer port (default: `8000`).
- `--interval`: Health check interval in seconds (default: `5`).
- `--config`: Path to the JSON configuration file for backend servers.

Example:
```bash
./lb --host 0.0.0.0 --port 8080 --interval 15 --config my_servers.json
```

---

## Example Workflow

1. Start three backend servers:
Simple http servers example
   ```bash
   python http.server 8001
   python http.server 8002
   python http.server 8003
   ```

2. Configure `servers.json` with their details.

3. Start the load balancer:
   ```bash
   ./lb --host 127.0.0.1 --port 8000 --interval 10 --config servers.json
   ```

4. Send requests to the load balancer:
   ```bash
   curl http://127.0.0.1:8000
   ```

5. Stop a backend server and observe the health checks. The load balancer will:
   - Exclude the stopped server.
   - Reintegrate it once it becomes healthy again.

---

## Key Design Aspects

### Multithreading

- **Health Checks**:
  Each backend server is monitored in a separate thread, allowing continuous health verification without blocking other operations.

- **Bidirectional Communication**:
  Two threads handle each connection:
  - Forwarding client requests to the backend.
  - Sending backend responses to the client.

- **Concurrency**:
  Multiple client requests are handled simultaneously, improving scalability and performance.

### Edge Cases Handled

- **No Active Servers**:
  Returns a `503 Service Unavailable` response if no healthy servers are available.
- **Server Recovery**:
  Reintegrates servers automatically upon recovery.
- **Fault Tolerance**:
  Logs and handles errors gracefully without crashing.
- **Connection Timeouts**:
  Detects and manages connection timeouts during server communication.

---

## Project Structure

```
load-balancer/
├── core/
│   ├── balancer.py               # Load balancer
│   ├── health_checker.py         # Health check logic
├── servers/
│   ├── server.py                 # Server loader
│   ├── servers.json              # Backend server configuration
├── lb                            # Command-line tool entry point
├── README.md                     # Documentation
```

---

## Acknowledgments

This project was developed as a solution to the [Load Balancer Coding Challenge](https://codingchallenges.fyi/challenges/challenge-load-balancer/), showcasing concepts of load balancing, fault tolerance, and multithreaded programming.

---
