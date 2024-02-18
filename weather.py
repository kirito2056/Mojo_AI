import requests
import json


def get_location():
    API_KEY = 'AIzaSyCfJ9JXotKNNqKpYX9ikQ3tkZB9AWDYfLg'

    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + API_KEY
    data = {}
    response = requests.post(url, json=data)
    print(response)

    if response.status_code == 200:
        result = response.json()
        print("위도:", result['location']['lat'])
        print("경도:", result['location']['lng'])
        return result['location']['lat'], result['location']['lng'], '안양'
    else:
        print("오류 발생:", response.status_code)

def get_weather(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&lat={latitude}&lon={longitude}"

    try:
        response = requests.get(complete_url).json()
    except requests.exceptions.RequestException as e:
        return e

    return response

def whatWeather():
    api_key = "50723333e4cced07bdba598be59049f4"
    latitude, longitude, city = get_location()
    weather = get_weather(api_key, latitude, longitude)

    print(f"Weather in {city}:")
    print(weather)

    extract_weather_info(weather)

    weather_text = weather
    return weather_text

def extract_weather_info(data):
    weather_info = data['weather'][0]
#    temp_info = data['main'][0]
    id_value = weather_info['id']
#    temp_value = temp_info - 273.15
    print(f'id: {id_value}')
#    print(f'temp: {temp_value}')

#get_location()
print(whatWeather())

