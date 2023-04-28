# @Jarvis 2.0
# nekumelon

from modules.speech.speechToText.speechToText import SpeechToText
from modules.speech.textToSpeech.textToSpeech import TextToSpeech
from modules.process.process import processQuery
from modules.state.state import State
from modules.memory.memory import Memory
from modules.cache.cache import Cache
from modules.plugins.plugins import pluginText
from modules.config.config import getConfig
from modules.debug.debug import debugMessage
from modules.events.events import beginEventLoop
import threading
import time, math
# import faulthandler

# faulthandler.enable()

debugMessage("Finished loading main modules. Loading config...")

config = getConfig("config.json")
debugMessage("Loaded config")

debugMessage("Creating speech to text...");
speechToText = SpeechToText()
debugMessage("Creating text to speech...");
textToSpeech = TextToSpeech(config['service'])
debugMessage("Finished creating text to speech and speech to text");

debugMessage("Creating memory...");
memory = Memory()

debugMessage("Creating cache...");
cache = Cache()

debugMessage("Finished creating cache and memory");

debugMessage("Creating state...");
state = State(speechToText, textToSpeech, memory)
state.config = config
debugMessage("Finished creating state");

eventLoopThread = threading.Thread(target=beginEventLoop)
eventLoopThread.start()

def processLoop():
    while state.listening:
        print("Listening...")
        
        if state.config["input"] == "text":
            query = input("Enter a query: ")
        else:
            audio = speechToText.listen()
            query = speechToText.recognize(audio, recognizer=config["recognizer"]);
            print('Query: ' + query)

        startTime = time.time();

        if not query:
            continue

        debugMessage("Processing query...")
        response = processQuery(query, state)
        debugMessage("Finished processing query")

        debugMessage("Adding to memory...");
        cache.set(query, response)

        debugMessage("Adding to cache...");
        memory.add(query, response)

        debugMessage("Finished adding to memory and cache");

        debugMessage("Pruning memory..."); 
        memory.shortTerm.prune()
        debugMessage("Finished pruning memory");

        debugMessage("Plugging in text...");
        response = pluginText(response)
        debugMessage("Finished plugging in text");

        endTime = time.time();
        debugMessage(f"Query to response took {math.ceil(endTime - startTime)} seconds");

        if state.config["output"] == "text":
            print(response)
        else:
            debugMessage("Speaking response")
            textToSpeech.speak(response)
            debugMessage("Finished speaking response")


try:
    if state.config["input"] == "text":
        debugMessage("Starting process loop")
        processLoop()
    else:
        debugMessage("Initializing microphone")

        with speechToText.microphone as source:
            speechToText.source = source

            debugMessage("Adjusting for ambient noise")
            speechToText.adjustForAmbient()
            debugMessage("Finished adjusting for ambient noise")

            debugMessage("Starting process loop")
            processLoop()

except KeyboardInterrupt:
    pass

debugMessage("Writing memory and cache");
memory.writeMemory()
cache.writeCache()
debugMessage("Finished writing memory and cache");