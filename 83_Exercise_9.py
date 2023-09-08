<<<<<<< HEAD
# Akhbaar Padhke Sunaao
from pip import main


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("You learn all new technology for your bright future")
=======
# # Akhbaar Padhke Sunaao
# from pip import main

import requests
import json
r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=802c00d5f36442c597a212ab1b213448')
z=r.json()

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

for article in z['articles']:
    print(article['title'])
    speak(article['title'])





>>>>>>> 8ad8ee1 (Add initial files)
