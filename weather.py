import requests
import json

def get_location():
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    return data['lat'], data['lon'], data['city']

def get_weather(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&lat={latitude}&lon={longitude}"
    response = requests.get(complete_url)
    return response.json()

api_key = ""

latitude, longitude, city = get_location()
weather = get_weather(api_key, latitude, longitude)

weather_text = 'I think about you a lot'



print("Weather in {city}:")
print(weather)
