from gtts import gTTS

text = "안녕하세요. 파이썬과 40개의 작풀들 입니다."

tts = gTTS(text=text, lang = 'ko')
tts.save(r"23pythonproject\chapter3\hi.mp3")