from gtts import gTTS
from playsound import playsound
import os

text = '히히히히히 오줌발사'
tts = gTTS(text = text , lang='ko')

fileName = "tovoice"
fileExtension = "mp3"

fullpath:str = fr"{os.getcwd()}/{fileName}.{fileExtension}".replace("\\","/")

tts.save(fullpath)

playsound(fullpath)