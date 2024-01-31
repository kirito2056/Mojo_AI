import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#음성 인식 - Sound To Text
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko-KR')
        print('[사용자] ' + text)
    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e))
