import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("자 말해보시오")
    recognizer.adjust_for_ambient_noise(source)

    try:
        audio = recognizer.listen(source, timeout=5)
    except sr.WaitTimeoutError:
        print("마이크가 당신의 목소리를 못듣고 있는거 같소")

try:
    text = recognizer.recognize_google(audio, language="ko-KR")
    print("인식된 텍스트: " + text)
except sr.UnknownValueError:
    print("뭐래는겨 똑바로 말해봐")
except sr.RequestError as e:
    print(f"이건 구글 오류인디 : {e}")
