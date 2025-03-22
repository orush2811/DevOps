Weather-Based Clothing Suggester
A web application that suggests what to wear based on the current weather conditions (temperature, humidity, wind speed) at your location. Built with Python/Flask, containerized with Docker, orchestrated with Kubernetes, and provisioned using Terraform.
Overview
This project is a practical microservices-based application that:
Detects your location (via manual input or IP-based geolocation in future iterations).

Fetches real-time weather data using the OpenWeatherMap API.

Provides clothing recommendations tailored to temperature, humidity, and wind speed.

Runs as a scalable, cloud-native app deployable on Kubernetes clusters.

Perfect for developers learning Flask, Docker, Kubernetes, and Terraform, or anyone who wants a handy tool to decide their daily outfit!
Features
Weather Integration: Pulls current weather data (temperature, humidity, wind speed) for any location.

Smart Suggestions: Clothing recommendations based on:
Temperature (e.g., heavy coat below 5°C, t-shirt above 15°C).

Humidity (e.g., waterproof gear if >80%).

Wind speed (e.g., windbreaker if >10 m/s).

Web Interface: Simple Flask-based UI for entering a location and viewing suggestions.

Cloud-Ready: Deployable on Kubernetes with Docker containers and Terraform-provisioned infrastructure (e.g., AWS EKS).

Tech Stack
```
Backend: Python 3.9, Flask

Containerization: Docker

Orchestration: Kubernetes

Infrastructure: Terraform (AWS EKS example)

API: OpenWeatherMap
```
Prerequisites
```
Python 3.9+

Docker

Kubernetes (e.g., Minikube for local testing)

Terraform

AWS CLI (if deploying to EKS)

An OpenWeatherMap API key (free tier available)
```
Setup Instructions
1. Clone the Repositor
```
bash

git clone https://github.com/yourusername/weather-clothes-app.git
cd weather-clothes-app
```
2. Install Dependencies
```
bash

pip install -r requirements.txt
```
3. Get an API Key
Sign up at OpenWeatherMap.

Copy your API key and set it as an environment variable:
```
bash

export WEATHER_API_KEY="your_api_key_here"
```
4. Run Locally (Flask)
```
bash

python app.py

Open http://localhost:5000 in your browser.
```
5. Dockerize the App
```
bash

docker build -t weather-clothes-app:latest .
docker run -p 5000:5000 -e WEATHER_API_KEY="your_api_key_here" weather-clothes-app
```
6. Deploy with Kubernetes (Local)
Start Minikube:
```
bash

minikube start
```
Apply Kubernetes manifests:
```
bash

kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml
```
Access the app:
```
bash

minikube service weather-app-service --url
```
7. Deploy to AWS EKS (Cloud)
Configure AWS CLI with your credentials.

Initialize Terraform:
bash

cd terraform
terraform init
terraform apply

Update kubectl to use the EKS cluster:
bash

aws eks update-kubeconfig --name weather-app-cluster --region us-east-1

Deploy the app:
bash

kubectl apply -f ../k8s/

Get the external IP from the service:
bash

kubectl get svc weather-app-service

Project Structure

weather-clothes-app/
├── app.py            # Flask app with weather API integration
├── logic.py          # Clothing suggestion logic (optional separation)
├── requirements.txt  # Python dependencies
├── templates/
│   └── index.html    # HTML frontend
├── Dockerfile        # Docker configuration
├── k8s/
│   ├── deployment.yaml  # Kubernetes deployment
│   └── service.yaml     # Kubernetes service
└── terraform/
    └── main.tf       # Terraform config for AWS EKS

Usage
Open the app in your browser (e.g., http://localhost:5000 locally).

Enter a city name (e.g., "New York") in the form.

Submit to see the current weather and a clothing suggestion based on temperature, humidity, and wind speed.

Example output:
Weather: 8°C, 85% humidity, 12 m/s wind

Suggestion: "A jacket and long pants are recommended. High humidity—consider waterproof clothing or an umbrella. Windy—add a windbreaker or hat."

Future Enhancements
Auto-detect user location using IP geolocation or browser API.

Add caching (e.g., Redis) for weather data to reduce API calls.

Improve UI with CSS or a frontend framework (e.g., React).

Store API keys securely with Kubernetes Secrets or AWS Secrets Manager.

Contributing
Feel free to fork this repo, submit issues, or send pull requests! Contributions are welcome.
License
This project is licensed under the MIT License—see the LICENSE file for details.

