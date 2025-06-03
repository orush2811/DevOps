# Simple Budget Calculator

A simple budget calculator application built with Node.js, Express, and MongoDB.

## Features

- Track income and expenses
- View running balance
- Add and delete transactions
- Track car payment expenses
- Automatic savings goal calculation (20% of monthly income)
- Smart financial recommendations
- Simple and intuitive interface
- Docker and Kubernetes support

## How It Works

The calculator helps you manage your finances by:
- Tracking all your monthly income and expenses
- Calculating your available balance after all expenses
- Automatically suggesting a monthly savings goal (20% of your income)
- Providing feedback on whether you can meet the recommended savings target
- Breaking down expenses by category for better financial planning

## Savings Calculator Feature

The budget calculator includes a smart savings recommendation system:

### Automatic Savings Goal
- Calculates a recommended monthly savings target (20% of your gross income)
- Based on the widely-used "20% savings rule" financial principle
- Helps users maintain a healthy savings habit

### Smart Feedback System
- Compares your available money after expenses with the recommended savings goal
- Provides visual indicators:
  - ✅ Green success message when you can meet the savings goal
  - ⚠️ Warning message if expenses need adjustment to meet the goal
- Shows the exact amount you can save based on current income and expenses

### Financial Health Indicators
- Displays savings goal as a percentage of your income
- Shows how much of your income remains after all expenses
- Helps identify if your expenses are too high relative to your savings goals

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