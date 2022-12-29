import speech_recognition as sr
import pygame
from gtts import gTTS
from chatgpt_wrapper import ChatGPT


def talk_to_chatGPT(words):
    tts = gTTS(text=words, lang='en', slow=False, tld='co.uk')
    tts.save(r'output.mp3')
    pygame.mixer.music.load(r'output.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    

r = sr.Recognizer()
speech = 'hello'
bot = ChatGPT()
pygame.mixer.init()

while True:
    with sr.Microphone(0) as source:    
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio, language='en-US')
        if speech == 'bye':
            goodbye_message = 'bye-bye'
            talk_to_chatGPT(goodbye_message)
            break
        
        for chunk in bot.ask_stream(speech):
            try:
                talk_to_chatGPT(chunk)
            except:
                pass
        speech = 'bye'
    except sr.UnknownValueError:
        print('could not understand audio')
    except sr.RequestError:
        print('Looks like, there is some problem with Google Speech Recognition')    
