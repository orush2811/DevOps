import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"] 
        }
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