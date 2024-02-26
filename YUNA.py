import requests
import json
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import sys

API_KEY = 'AIzaSyCfJ9JXotKNNqKpYX9ikQ3tkZB9AWDYfLg'
API_WEATHER_KEY = "50723333e4cced07bdba598be59049f4"

# Functions from 'readWeatherData.py'
def find_weather_data(id):
    with open('weather.json') as f:
        data = json.load(f)
        
        for forecast_list in data.values():
            for forecast in forecast_list:
                if forecast['id'] == id:
                    print(f"log: {forecast['log']}")
                    return forecast['status']

def get_status_from_id(id):
    status = find_weather_data(id)
    if status:
        return status
    else:
        return None

# Functions from 'textToSpeech.py'
def speak(text):
    print('[인공지능] ' + text)
    tts = gTTS(text=text, lang='ko')
    tts.save('voice.mp3')
    playsound('voice.mp3')

# Functions from 'whatWhather.py'
def get_location():
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + API_KEY
    data = {}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['location']['lat'], result['location']['lng']
    else:
        print("오류 발생:", response.status_code)

def weather_info(data):
    weather_info = data['weather'][0]
    id_value = weather_info['id']
    return id_value

def temp_info(data):
    temp_value = data['main']['temp']
    return temp_value

def get_weather(api_key, latitude, longitude):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&lat={latitude}&lon={longitude}"

    try:
        response = requests.get(complete_url).json()
    except requests.exceptions.RequestException as e:
        return e

    return response

def whatWeather():
    latitude, longitude = get_location()
    weather = get_weather(API_WEATHER_KEY, latitude, longitude)

    weather_id = str(weather_info(weather))
    temp = str(temp_info(weather))

    return find_weather_data(weather_id)

def weatherAnswer(temp):
    if temp < 0:
        answer_text = "온도 기준을 몇으로 해야할까"
    return answer_text

# Main answer function
def answer(input_text):
    answer_text = ''
    if input_text is None:
        answer_text = '음성 인식에 실패했습니다. 다시 시도해주세요.'
    elif '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        if '오늘' in input_text:
            answer_text = '현재 날씨는' + str(whatWeather())
        elif '내일' in input_text:
            answer_text = '내일 날씨는 이렇습니다'
        elif '월' or '일' in input_text:
            if '월요일' in input_text:
                answer_text = '요일별 날씨는 아직 구현되지 않은 기능입니다'
                pass
            #text에서 월, 일 앞의 숫자 찾는 알고리즘
            answer_text = whatWeather()
    elif '저리가' in input_text:
            sys.exit()
    else:
        answer_text = '다시 한번 말씀해주세요'
    
    speak(answer_text)

# Main loop for conversation
def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        with microphone as source:
            audio = recognizer.listen(source)

        try:
            recognized_text = recognizer.recognize_google(audio, language='ko-KR')
            print("인식된 텍스트:", recognized_text)
            answer(recognized_text)
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
        except sr.RequestError as e:
            print("음성 인식 서비스에 접근할 수 없습니다:", e)

if __name__ == "__main__":
    speak('듣고있어요')
    main()
