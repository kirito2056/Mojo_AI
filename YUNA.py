import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import whatWhather
import sys

#음성 인식 - Sound To Text
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko-KR')
        print('[사용자] ' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')
        answer('다시 한번 말씀해주세요')
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e))

#대답 생성
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        if '오늘' in input_text:
            answer_text = '핫스팟에 연결되어있을경우 위치가 특정되지 않을수도 있습니다' + str(whatWhather.whatWeather())
        elif '내일' in input_text:
            answer_text = '내일 날씨는 이렇습니다'
        elif '월' or '일' in input_text:
            if '월요일' in input_text:
                answer_text = '요일별 날씨는 아직 구현되지 않은 기능입니다'
                pass
            #text에서 월, 일 앞의 숫자 찾는 알고리즘
            answer_text = whatWhather.weatherText()
        elif '저리가'in input_text:
            sys.exit()
    else:
        answer_text = '다시 한번 말씀해주세요'
    speak(answer_text)

#대답 출력 - Text To Sound
def speak(text):
    print('[인공지능] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)

r = sr.Recognizer()
m = sr.Microphone(energy_threshold=100)

#백그라운드에서 마이크 사용 설정
speak('듣고있어요')
stop_listening = r.listen_in_background(m, listen)

#무한 반복
while True:
    time.sleep(0.1)