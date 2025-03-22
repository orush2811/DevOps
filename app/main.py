from flask import Flask, request, jsonify, render_template
from weather import get_current_weather, get_week_forecast, clothing_suggestion
from datetime import datetime

app = Flask(__name__)
API_KEY = "ad1cad1d990490bb4b9efc6469e2f503"

@app.route('/clothing', methods=['GET'])
def get_clothing_advice_api():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city"}), 400
    current_weather = get_current_weather(city, API_KEY)
    if not current_weather:
        return jsonify({"error": "Could not fetch current weather data"}), 503
    week_forecast = get_week_forecast(city, API_KEY)
    if not week_forecast:
        return jsonify({"error": "Could not fetch forecast data"}), 503
    current_suggestion = clothing_suggestion(current_weather["temp"], current_weather["humidity"], current_weather["wind_speed"])
    forecast_suggestions = {
        date.strftime("%Y-%m-%d"): {
            **data,
            "clothing_suggestion": clothing_suggestion(data["temp"], data["humidity"], data["wind_speed"])
        } for date, data in week_forecast.items()
    }
    return jsonify({
        "city": city,
        "current": {**current_weather, "clothing_suggestion": current_suggestion},
        "forecast": forecast_suggestions
    })

@app.route('/', methods=['GET', 'POST'])
def index():
    city = request.form.get('city') if request.method == 'POST' else request.args.get('city', 'London')
    error = None
    data = {"city": city, "current": None, "forecast": {}}

    current_weather = get_current_weather(city, API_KEY)
    if not current_weather:
        error = "Could not fetch current weather data."
    else:
        data["current"] = {
            **current_weather,
            "clothing_suggestion": clothing_suggestion(current_weather["temp"], current_weather["humidity"], current_weather["wind_speed"])
        }

    week_forecast = get_week_forecast(city, API_KEY)
    if not week_forecast:
        if not error:
            error = "Could not fetch forecast data."
    else:
        data["forecast"] = {
            date.strftime("%Y-%m-%d"): {
                **data,
                "clothing_suggestion": clothing_suggestion(data["temp"], data["humidity"], data["wind_speed"])
            } for date, data in week_forecast.items()
        }

    return render_template('index.html', data=data, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)