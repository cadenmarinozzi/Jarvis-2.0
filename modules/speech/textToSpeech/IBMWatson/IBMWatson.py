from simpleSound import play
from dotenv import load_dotenv
from modules.utils.formatForTTS import formatForTTS
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os, requests, pyaudio

load_dotenv()

WATSON_API_KEY = os.getenv('WATSON_API_KEY')
SERVICE_URL = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com'

CHANNELS = 1
RATE = 22050 # WAV Audio rate
FORMAT = pyaudio.paInt16

authenticator = IAMAuthenticator(WATSON_API_KEY);
service = TextToSpeechV1(authenticator=authenticator)
service.set_service_url(SERVICE_URL)

class TTSSynthesizeCallback(SynthesizeCallback):
    def __init__(self):
        SynthesizeCallback.__init__(self)

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_audio_stream(self, audioStream):
        if (self.firstChunk):
            self.firstChunk = False;

            return;
    
        self.stream.write(audioStream)

    def createStream(self):
        self.firstChunk = True;

        self.audioHandler = pyaudio.PyAudio()
        self.stream = self.audioHandler.open(format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            output=True
        )

    def closeAudioHandler(self):
        self.audioHandler.terminate()

synthesizeCallback = TTSSynthesizeCallback()

def createTextToSpeechWav(text):
    text = formatForTTS(text)

    url = f"{SERVICE_URL}/instances/e8987052-c166-4039-bdf3-1bd77aa91a32/v1/synthesize?voice=en-GB_JamesV3Voice"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'audio/wav',
    }
    data = '{"text": "' + text + '"}'

    response = requests.post(url, headers=headers, data=data, auth=('apikey', WATSON_API_KEY))

    return response.content

def createAndPlayTextToSpeechWav(text):
    wav = createTextToSpeechWav(text)

    with open("speech.wav", "wb") as file:
        file.write(wav)

    play("speech.wav")

def createAndStreamTextToSpeech(text):
    synthesizeCallback.createStream()

    service.synthesize_using_websocket(text,
        synthesizeCallback,
        accept='audio/wav',
        voice='en-GB_JamesV3Voice'
    )

    synthesizeCallback.closeAudioHandler()
