import speech_recognition as sr
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("말하세요...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="ko-KR")
    print("인식된 텍스트: " + text)
except sr.UnknownValueError:
    print("음성을 인식할 수 없습니다.")
except sr.RequestError as e:
    print(f"Google Web Speech API 오류: {e}")
