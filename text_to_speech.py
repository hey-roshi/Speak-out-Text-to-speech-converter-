from gtts import gTTS
from playsound import playsound

def textToAudio(str):
    audio = gTTS(str)
    audio.save('voice.mp3')


textToAudio('this is an example of text to voice converter')

playsound('voice.mp3')