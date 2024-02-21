import pyaudio
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

def transcribe_microphone():
    client = speech_v1.SpeechClient()

    # PyAudio를 사용하여 마이크로부터 오디오 스트림을 캡처합니다.
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("Listening...")

    # 오디오 스트림에서 데이터를 읽어 Google Cloud Speech-to-Text API로 전송합니다.
    while True:
        data = stream.read(chunk)
        audio_input = {"content": data}
        config = {
            "language_code": "ko-KR",
            "audio_channel_count": 1,
        }
        response = client.recognize(config=config, audio=audio_input)
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))

    stream.stop_stream()
    stream.close()
    audio.terminate()

if __name__ == "__main__":
    transcribe_microphone()
