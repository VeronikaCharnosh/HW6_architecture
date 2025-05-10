# HW6_architecture


This repository contains two FastAPI-based microservices that work together to compute recommended daily water intake and simulate client-server interaction using Podman Compose.

---

## ⚙️ Pre-setup: Podman Installation

### macOS
Install Podman and Podman Compose via Homebrew:
```bash
brew install podman podman-compose
```
## Task 1 — Containerizing the Business Logic Service


This task focuses on containerizing the business_service, which calculates recommended water intake based on weight and activity level.

Test Business Service
1. Build the image
```bash
cd HW6
podman build -t business-service -f Dockerfile .
```
2. Run the container
```bash
podman run -d -p 8001:8000 --name business-service business-service
```
3. Test the endpoint
```bash
curl http://localhost:8001/health
```
Expected response:
```
{"status": "ok"}
```


## Task 2 — Multi-Container Setup with Podman Compose


This task integrates two services (business_service and client_service) using podman-compose.

How to Build and Run
1. Navigate to project root
```bash
cd HW6
```
2. Run services
```bash
podman compose up --build
```
3. Check status
```bash
podman ps
```
4. View logs
```bash
podman logs hw6-client_service-1
podman logs hw6-business_service-1
```
Test Full Flow
Send a calculation request through the client service:

```bash
curl -X POST http://localhost:8000/calculate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SuperSecretToken" \
  -d '{"weight": 65, "activity_level": "high"}'
```

Expected response:

```json
{
  "weight": 65.0,
  "activity_level": "high",
  "recommended_water_liters": 2.6
}
```

Clean Up
Stop and remove containers
```bash
podman compose down
```



