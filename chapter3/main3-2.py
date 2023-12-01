from gtts import gTTS
from playsound import playsound

file_path = r"23pythonproject\chapter3\나의텍스트.txt"
with open(file_path,'rt', encoding = 'UTF8')as f:
    read_file = f.read()

print(read_file)

tts = gTTS(text=read_file, lang="ko")
tts.save(r"23pythonproject\나의 텍스트.mp3")

playsound(r"23pythonproject\나의 텍스트.mp3")