# Akhbaar Padhke Sunaao
from pip import main


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("You learn all new technology for your bright future")