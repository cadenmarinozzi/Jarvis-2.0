import speech_recognition as sr, subprocess, os
from dotenv import load_dotenv

load_dotenv();

class SpeechToText:
    def __init__(self, ambientAdjustDuration=2, language='en-US'):
        self.recognizer = sr.Recognizer();
        self.microphone = sr.Microphone(device_index=len(sr.Microphone.list_microphone_names()) - 1);

        self.ambientAdjustDuration = ambientAdjustDuration;
        self.language = language;

    def adjustForAmbient(self):
        self.recognizer.adjust_for_ambient_noise(self.source, duration=self.ambientAdjustDuration);

    def recognize(self, audio, recognizer='google'):
        try:
            if recognizer == 'google':
                recognized = self.recognizer.recognize_google(audio, language=self.language);
            elif recognizer == 'whisper-local':
                recognized = self.recognizer.recognize_whisper(audio, language=self.language);
            elif recognizer == 'whisper':
                recognized = self.recognizer.recognize_whisper_api(audio, language=self.language, api_key=os.getenv('OPENAI_API_KEY'));
            
            return recognized;
        except sr.UnknownValueError:
            return;

    def listen(self):
        audio = self.recognizer.listen(self.source);

        return audio;