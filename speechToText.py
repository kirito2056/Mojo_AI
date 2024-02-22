import speech_recognition as sr

recognizer = sr.Recognizer()

def listen(recognizer, audio):
    with sr.Microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        recognized_text = recognizer.recognize_google(audio, language = 'ko-KR')
        return recognized_text
    except sr.UnknownValueError as e:
        return '에러 발생 : {0}'.format(e)
    except sr.RequestError as e:
        return '에러 발생 : {0}'.format(e)