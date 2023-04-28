import pyttsx3
from .IBMWatson.IBMWatson import createAndPlayTextToSpeechWav, createAndStreamTextToSpeech

class TextToSpeech:
    def __init__(self, service="pyttsx3"):
        self.service = service

    def speak(self, text):
        if self.service == "pyttsx3":
            pyttsx3.speak(text)
        elif self.service == 'ibm-watson':
            # createAndPlayTextToSpeechWav(text)
            createAndStreamTextToSpeech(text)