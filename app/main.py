from flask import Flask, request, render_template
import requests
import os
from datetime import datetime, timedelta
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from flask_debugtoolbar import DebugToolbarExtension
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
toolbar = DebugToolbarExtension(app)

# Prometheus metrics
WEATHER_REQUESTS = Counter('weather_requests_total', 'Total weather API requests', ['location'])
WEATHER_REQUEST_LATENCY = Histogram('weather_request_duration_seconds', 'Weather API request duration')
API_ERRORS = Counter('weather_api_errors_total', 'Total weather API errors')

API_KEY = os.getenv("WEATHER_API_KEY", "API_KEY")  # Your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_weather_forecast(location):
    WEATHER_REQUESTS.labels(location=location).inc()
    with WEATHER_REQUEST_LATENCY.time():
        params = {"q": location, "appid": API_KEY, "units": "metric"}
        print(f"Using API Key: {API_KEY}")  # Debug line
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        API_ERRORS.inc()
        print(f"API call failed with status: {response.status_code}")  # Debug line
        return None

def suggest_clothes(temp, humidity, wind_speed, rain, clouds, description):
    suggestion = []
    # Temperature
    if temp < 5:
        suggestion.append("Wear a heavy coat, scarf, and gloves.")
    elif 5 <= temp <= 15:
        suggestion.append("A jacket and long pants are recommended.")
    else:
        suggestion.append("A t-shirt or light sweater is fine.")
    
    # Humidity
    if humidity > 80:
        suggestion.append("High humidity—consider waterproof clothing or an umbrella.")
    elif humidity < 30:
        suggestion.append("Low humidity—moisturizer might help your skin!")
    
    # Wind Speed
    if wind_speed > 10:
        suggestion.append("Windy—add a windbreaker or hat.")
    
    # Rain (precipitation in mm over 3 hours)
    if rain > 0:
        if rain > 5:
            suggestion.append("Heavy rain expected—bring a raincoat and waterproof shoes.")
        else:
            suggestion.append("Light rain possible—carry an umbrella.")
    
    # Cloudiness
    if clouds > 80:
        suggestion.append("Very cloudy—might feel cooler than it is.")
    elif clouds < 20:
        suggestion.append("Mostly clear—sunglasses could be handy.")
    
    # Weather Description (e.g., "light rain", "snow")
    if "snow" in description.lower():
        suggestion.append("Snow expected—wear insulated boots and layers.")
    elif "thunderstorm" in description.lower():
        suggestion.append("Thunderstorm possible—stay cautious and dry.")
    
    return " ".join(suggestion) if suggestion else "No specific suggestions—just dress comfortably!"

def process_forecast(data):
    forecast_list = data["list"]
    daily_forecasts = []
    today = datetime.now().date()
    
    for i in range(5):  # Next 5 days
        target_date = today + timedelta(days=i)
        target_date_str = target_date.strftime("%Y-%m-%d")
        
        for forecast in forecast_list:
            forecast_time = forecast["dt_txt"]
            if target_date_str in forecast_time and "12:00:00" in forecast_time:
                temp = forecast["main"]["temp"]
                humidity = forecast["main"]["humidity"]
                wind_speed = forecast["wind"]["speed"]
                rain = forecast.get("rain", {}).get("3h", 0)  # Rain in mm over 3 hours, default 0
                clouds = forecast["clouds"]["all"]  # Cloudiness in %
                description = forecast["weather"][0]["description"]  # e.g., "light rain"
                icon = forecast["weather"][0]["icon"]  # Icon code (e.g., "10d")
                suggestion = suggest_clothes(temp, humidity, wind_speed, rain, clouds, description)
                
                daily_forecasts.append({
                    "date": target_date_str,
                    "temp": temp,
                    "humidity": humidity,
                    "wind_speed": wind_speed,
                    "rain": rain,
                    "clouds": clouds,
                    "description": description,
                    "icon": f"http://openweathermap.org/img/wn/{icon}@2x.png",  # Icon URL
                    "suggestion": suggestion
                })
                break
    
    return daily_forecasts

@app.route("/", methods=["GET", "POST"])
def home():
    forecast_data = None
    location = "London"  # Default location
    if request.method == "POST":
        location = request.form.get("location", "London")
        print(f"Form submitted with location: {location}")  # Debug line
        weather_data = get_weather_forecast(location)
        if weather_data:
            forecast_data = process_forecast(weather_data)
    return render_template("index.html", forecast_data=forecast_data, location=location)

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)