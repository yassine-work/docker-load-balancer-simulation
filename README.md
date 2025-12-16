<div align="center">

# 🐳 Docker Load Balancer Simulation

### A practical Layer 7 load balancing architecture using Nginx and Docker

[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

</div>

---

## 📖 Overview

This project demonstrates how to distribute incoming HTTP traffic across multiple backend servers using **Nginx** as a reverse proxy load balancer. It answers a fundamental question in distributed systems: *"How do we handle traffic when one server isn't enough?"*

### Key Features

- **Round Robin Load Balancing** – Distributes requests evenly across servers
- **Fault Tolerance** – Automatic failover when servers go down
- **Easy Scaling** – Add or remove servers with a single command
- **Isolated Network** – All services communicate within a private Docker network

---

## 🏗️ Architecture

```
┌─────────────┐
│   Client    │
│  (Browser)  │
└──────┬──────┘
       │
       │ HTTP Request (Port 8080)
       │
┌──────▼──────────────────────┐
│    Nginx Load Balancer      │
│     (Round Robin)            │
└──────┬──────────────────────┘
       │
       ├─────────┬─────────┬
       │         │         │         
  ┌────▼───┐ ┌──▼────┐ ┌──▼────┐
  │ Flask  │ │ Flask │ │ Flask │
  │ App 1  │ │ App 2 │ │ App 3 │
  └────────┘ └───────┘ └───────┘
```

**Components:**
- **Client:** Your web browser making HTTP requests
- **Load Balancer:** Nginx reverse proxy listening on port 8080
- **Backend Servers:** Three Flask application instances
- **Network:** Private Docker bridge network for service communication

---

## 📁 Project Structure

```
docker-load-balancer-simulation/
├── app.py                 # Flask backend application
├── Dockerfile             # Container image definition
├── nginx.conf             # Nginx upstream configuration
├── docker-compose.yml     # Service orchestration
└── README.md              # This file
```

---

## 🚀 Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running

### Quick Start

**1. Clone the repository**

```bash
git clone https://github.com/yassine-work/docker-load-balancer-simulation.git
cd docker-load-balancer-simulation
```

**2. Start the cluster**

```bash
docker compose up --build
```

This command will:
- Build the Flask application image
- Start 3 backend server replicas
- Launch the Nginx load balancer
- Create an isolated Docker network

**3. Verify it's running**

You should see logs indicating all services are active:

```
✓ app-1  | Running on http://0.0.0.0:5000
✓ app-2  | Running on http://0.0.0.0:5000
✓ app-3  | Running on http://0.0.0.0:5000
✓ nginx  | ready to accept connections
```

---

## 🧪 Testing & Experiments

### Test 1: Load Balancing in Action

**Objective:** Verify that requests are distributed across servers

1. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

2. Refresh the page multiple times (Press F5)

3. **Expected Result:** The server ID changes with each request
   ```
   Request 1: Response from Server: e12a3b4c...
   Request 2: Response from Server: 99c8d7f1...
   Request 3: Response from Server: 7a2f5e9d...
   ```

---

### Test 2: Fault Tolerance (Chaos Engineering)

**Objective:** Verify the system remains available when a server fails

1. While the app is running, open a new terminal

2. List running containers:
   ```bash
   docker ps
   ```

3. Stop one backend container:
   ```bash
   docker stop <container_id>
   ```

4. Return to your browser and refresh

**Expected Result:** The application continues to work seamlessly. Nginx automatically detects the failure and routes traffic only to healthy servers.

---

### Test 3: Dynamic Scaling

**Objective:** Scale the backend to handle increased traffic

1. Edit `docker-compose.yml` and change:
   ```yaml
   replicas: 3  →  replicas: 5
   ```

2. Apply the changes:
   ```bash
   docker compose up -d --scale app=5
   ```

3. Verify new containers are running:
   ```bash
   docker ps
   ```

**Expected Result:** Nginx automatically discovers the new servers and includes them in the rotation.

---

## 🎓 Learning Outcomes

This project demonstrates essential concepts in distributed systems:

| Concept | Implementation |
|---------|----------------|
| **Load Balancing** | Nginx upstream module with round-robin algorithm |
| **Service Discovery** | Docker Compose DNS resolution |
| **Stateless Design** | Backend servers don't store session data |
| **High Availability** | Automatic failover to healthy servers |
| **Horizontal Scaling** | Add/remove servers without downtime |
| **Container Orchestration** | Docker Compose for multi-container apps |

---

## 🛠️ How It Works

### Round Robin Algorithm

Nginx cycles through the upstream servers sequentially:

```
Request 1 → Server A
Request 2 → Server B  
Request 3 → Server C
Request 4 → Server A (cycle repeats)
```




## 📊 Key Configuration Files

### nginx.conf

```nginx
upstream backend {
    server app-1:5000;
    server app-2:5000;
    server app-3:5000;
}

server {
    listen 80;
    
    location / {
        proxy_pass http://backend;
    }
}
```

### docker-compose.yml

```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "8080:80"
    networks:
      - app-network
      
  app:
    build: .
    deploy:
      replicas: 3
    networks:
      - app-network
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

**Built with ❤️ for learning distributed systems**

[⬆ Back to Top](#-docker-load-balancer-simulation)

</div>