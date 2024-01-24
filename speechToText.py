import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("자 말해보시오")
    recognizer.adjust_for_ambient_noise(source)

    try:
        #음성 인식 및 text 변수에 저장
        audio = recognizer.listen(source, timeout=5)
        text = recognizer.recognize_google(audio, language="ko-KR")
        print("인식된 텍스트: " + text)

    except sr.WaitTimeoutError:
        print("5초 안에 말하지 않았군")
        text = None
    except sr.UnknownValueError:
        print("뭐래는겨 똑바로 말해봐")
        text = None
    except sr.RequestError as e:
        print(f"이건 구글 오류인디 : {e}")
        text = None

