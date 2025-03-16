from flask import Flask, request, jsonify
from weather import get_weather, clothing_suggestion

app = Flask(__name__)
API_KEY = "your_openweathermap_api_key_here"

@app.route('/clothing', methods=['GET'])
def get_clothing_advice():
    city = request.args.get('city', 'London')
    weather = get_weather(city, API_KEY)
    if weather:
        suggestion = clothing_suggestion(weather["temp"], weather["humidity"], weather["wind_speed"])
        return jsonify({"city": city, **weather, "clothing_suggestion": suggestion})
    return jsonify({"error": "Could not fetch weather data"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)