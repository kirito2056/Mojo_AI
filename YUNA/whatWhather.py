import requests
import YUNA.readWeatherData as readWeatherData

def get_location():
    API_KEY = 'AIzaSyCfJ9JXotKNNqKpYX9ikQ3tkZB9AWDYfLg'

    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + API_KEY
    data = {}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['location']['lat'], result['location']['lng']
    else:
        print("오류 발생:", response.status_code)

#날씨, 온도
def weather_info(data):
    weather_info = data['weather'][0]
    id_value = weather_info['id']
    return id_value

def temp_info(data):
    temp_value = data['main']['temp']
    return temp_value

#위도, 경도로 날씨 데이터 받아오기
def get_weather(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&lat={latitude}&lon={longitude}"

    try:
        response = requests.get(complete_url).json()
    except requests.exceptions.RequestException as e:
        return e

    return response

#이 파일의 메인함수라고 할 수 있는애
def whatWeather():
    api_key = "50723333e4cced07bdba598be59049f4"
    latitude, longitude = get_location()
    weather = get_weather(api_key, latitude, longitude)

    weather_id = str(weather_info(weather))
    temp = str(temp_info(weather))

    return readWeatherData.find_weather_data(weather_id)

    weather_text = weather_id + temp
    return weather_text
