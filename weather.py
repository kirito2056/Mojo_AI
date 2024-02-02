import requests
import json

def get_location():
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    return data['lat'], data['lon'], data['city']

# 사용 예시


latitude, longitude, city = get_location()


print("Weather in {city}:")
