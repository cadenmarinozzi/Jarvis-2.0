class State:
    def __init__(self, speechToText, textToSpeech, memory, name='Jarvis'):
        self.name = name;
        self.listening = True;

        self.speechToText = speechToText;
        self.textToSpeech = textToSpeech;

        self.memory = memory;