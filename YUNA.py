import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#음성 인식 - Sound To Text
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko-KR')
        print('[사용자] ' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e))

#대답 생성
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        if '오늘' in input_text:
            answer_text = '아직 구현중인 기능이예요'
        elif '내일' in input_text:
            answer_text = '내일 날씨는 이렇습니다'
        elif '월' or '일' in input_text:
            #text에서 월, 일 앞의 숫자 찾는 알고리즘
            answer_text = '월 일 날씨는 이렇습니다'
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
m = sr.Microphone()

stop_listening = r.listen_in_background(m, listen)

while True:
    time.sleep(0.1)