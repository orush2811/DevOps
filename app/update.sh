#!/bin/bash
echo "Building updated Docker image..."
docker build -t weather-app:latest .

echo "Loading image into Minikube..."
minikube image load weather-app:latest

echo "Restarting pods..."
kubectl delete pod -l app=weather-app

echo "Waiting for pods to restart..."
sleep 5  # Give Kubernetes a moment to recreate pods

echo "Updated app URL:"
minikube service weather-app-service --url