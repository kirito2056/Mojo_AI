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
        answer_text = '아직 개발해야 하는 기능입니다' 
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
