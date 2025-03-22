import requests
from datetime import datetime
from requests.exceptions import RequestException

def get_current_weather(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    except RequestException:
        return None

def get_week_forecast(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        daily_forecasts = {}
        for forecast in data["list"]:
            date = datetime.fromtimestamp(forecast["dt"]).date()
            if date not in daily_forecasts:
                daily_forecasts[date] = {
                    "temp": forecast["main"]["temp"],
                    "humidity": forecast["main"]["humidity"],
                    "wind_speed": forecast["wind"]["speed"]
                }
        return daily_forecasts
    except RequestException:
        return None

def clothing_suggestion(temp, humidity, wind_speed):
    base_suggestion = ""
    extras = []
    if temp < 5:
        base_suggestion = "Wear a heavy coat and warm layers."
    elif 5 <= temp < 15:
        base_suggestion = "A jacket or sweater should be good."
    elif 15 <= temp < 25:
        base_suggestion = "A light shirt will work."
    else:
        base_suggestion = "Go for a t-shirt and shorts."
    if humidity > 80:
        extras.append("Bring a waterproof jacket.")
    if wind_speed > 10:
        extras.append("Add a windbreaker.")
    return f"{base_suggestion} {' '.join(extras)}".strip()