from gtts import gTTS

with open('yuna.txt', 'r', encoding='utf8') as f:
    text = f.read() 


file_name = 'sample.mp3'

tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name)
