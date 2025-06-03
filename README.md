# Simple Budget Calculator

A simple budget calculator application built with Node.js, Express, and MongoDB.

## Features

- Track income and expenses
- View running balance
- Add and delete transactions
- Track car payment expenses
- Simple and intuitive interface
- Docker and Kubernetes support

## Prerequisites

- Node.js (v12 or higher)
- Docker and Docker Compose
- Kubernetes cluster (minikube for local development)
- kubectl CLI

## Local Development with Docker Compose

1. Build and start the containers:
```bash
docker-compose up --build
```

2. Access the application at:
```
http://localhost:3000
```

## Kubernetes Deployment

1. Start your Kubernetes cluster (e.g., minikube):
```bash
minikube start
```

2. Build the application Docker image:
```bash
docker build -t budget-app:latest .
```

3. Apply the Kubernetes manifests:
```bash
kubectl apply -f k8s/mongodb.yaml
kubectl apply -f k8s/app.yaml
```

4. Wait for the pods to be ready:
```bash
kubectl get pods -w
```

5. Access the application:
```bash
# If using minikube:
minikube service budget-app
```

## Directory Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── index.js
├── k8s/
│   ├── app.yaml
│   └── mongodb.yaml
├── package.json
└── public/
    └── index.html
```

## API Endpoints

- GET `/api/transactions` - Get all transactions
- POST `/api/transactions` - Add a new transaction
- DELETE `/api/transactions/:id` - Delete a transaction
- GET `/api/summary` - Get financial summary

## Scaling

The application is configured to run with 2 replicas in Kubernetes by default. You can scale it using:
```bash
kubectl scale deployment budget-app --replicas=3
``` 