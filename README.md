# **Weather-Based Clothing Suggester**
A web application that suggests what to wear based on the current weather conditions (temperature, humidity, wind speed) at your location. Built with Python/Flask, containerized with Docker, orchestrated with Kubernetes, and provisioned using Terraform (currently running locally).

# **Overview**
This project is a practical microservices-based application that:
- Detects your location (via manual input or IP-based geolocation in future iterations)
- Fetches current weather data for that location
- Analyzes weather conditions
- Suggests appropriate clothing
- Includes real-time code updates and monitoring capabilities

# **Features**
- Weather-based clothing suggestions
- 5-day weather forecast
- Real-time code updates (hot reloading)
- Monitoring with Prometheus and Grafana
- Metrics collection for:
  - Weather API requests
  - API latency
  - Error rates

# **Prerequisites**
- Docker and Docker Compose
- OpenWeather API key (sign up at https://openweathermap.org/api)

# **Setup Instructions**

1. Clone the repository:
```bash
git clone [repository-url]
cd weather-application
```

2. Create a `.env` file in the `app` directory with your API credentials:
```bash
WEATHER_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
FLASK_ENV=development
FLASK_DEBUG=1
```

3. Build and start the containers:
```bash
docker-compose up --build
```

# **Accessing the Services**

- Weather Application: http://localhost:8080
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000
  - Default login: admin/admin

# **Development with Hot Reloading**

The application is configured with hot reloading enabled. Any changes made to the Python files in the `app` directory will be automatically detected and the application will reload with your changes. This allows for rapid development and testing.

# **Monitoring with Grafana and Prometheus**

The application includes built-in monitoring capabilities:

1. **Metrics Available:**
   - Total weather requests (`weather_requests_total`)
   - API request latency (`weather_request_duration_seconds`)
   - API errors (`weather_api_errors_total`)

2. **Setting up Grafana:**
   - Access Grafana at http://localhost:3000
   - Log in with username: `admin`, password: `admin`
   - Add Prometheus as a data source:
     - URL: http://prometheus:9090
     - Access: Browser

3. **Viewing Metrics:**
   - Create new dashboards in Grafana to visualize:
     - Request rates
     - Response times
     - Error rates
     - API usage patterns

# **Architecture**

The application runs three main services:
1. **Flask Application (Port 8080)**
   - Handles weather data fetching and clothing suggestions
   - Implements hot reloading for development
   - Exposes metrics endpoint for Prometheus

2. **Prometheus (Port 9090)**
   - Collects and stores metrics
   - Provides query interface for Grafana

3. **Grafana (Port 3000)**
   - Visualizes metrics from Prometheus
   - Provides customizable dashboards
   - Supports alerting capabilities

# **Contributing**

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

# **Tech Stack**
```
Backend: Python 3.9, Flask

Containerization: Docker

Orchestration: Kubernetes

Infrastructure: Terraform (AWS EKS example)

API: OpenWeatherMap
```
# **Project Structure**

- weather-clothes-app/
  - app.py - Flask app with weather API integration
  - logic.py - Clothing suggestion logic (optional separation)
  - requirements.txt - Python dependencies
  - templates/
    - index.html - HTML frontend
  - Dockerfile - Docker configuration
  - k8s/
    - deployment.yaml - Kubernetes deployment
    - service.yaml - Kubernetes service
  - terraform/
    - main.tf - Terraform config for AWS EKS

# **Usage**
Open the app in your browser (e.g., http://localhost:8080 locally).

Enter a city name (e.g., "New York") in the form.

Submit to see the current weather and a clothing suggestion based on temperature, humidity, and wind speed.

## **Example output:**
Weather: 8°C, 85% humidity, 12 m/s wind

Suggestion: "A jacket and long pants are recommended. High humidity—consider waterproof clothing or an umbrella. Windy—add a windbreaker or hat."

# **Future Enhancements**
Auto-detect user location using IP geolocation or browser API.

Add caching (e.g., Redis) for weather data to reduce API calls.

Improve UI with CSS or a frontend framework (e.g., React).

Store API keys securely with Kubernetes Secrets or AWS Secrets Manager.

# **License**
This project is licensed under the MIT License—see the LICENSE file for details.

