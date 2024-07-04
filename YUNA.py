import requests
import json
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import sys

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

def speak(text):
    print('[인공지능] ' + text)
    tts = gTTS(text=text, lang='en')
    tts.save('voice.mp3')
    playsound('voice.mp3')

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
    
    weatherAnswer(temp)

    return find_weather_data(weather_id)

def weatherAnswer(temp):
    if temp < 0:
        answer_text = "추운 날씨네요. 따뜻하게 입고 나가세요"
    elif 0 <= temp < 10:
        answer_text = "쌀쌀한 날씨예요. 외투를 챙겨야 할 것 같아요"
    elif 10 <= temp < 20:
        answer_text = "서늘한 날씨예요. 가볍게 입고 나가도 좋을거같아요"
    elif 20 <= temp < 25:
        answer_text = "시원한 날씨네요. 밖에 나가서 산책하기 딱 좋은 날씨예요"
    elif 25 <= temp < 30:
        answer_text = "따뜻한 날씨네요. 햇빛을 즐기기 좋은 하루예요"
    elif 30 <= temp:
        answer_text = "더운 날씨예요. 시원하게 입고 나가는게 어떨까요?"
    return answer_text

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
            answer_text = whatWeather()
    elif '저리가' in input_text:
            speak('인공지능을 종료할게요')
            sys.exit()
    else:
        answer_text = '다시 한번 말씀해주세요'
    
    speak(answer_text)

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
