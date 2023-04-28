from .longTerm import LongTerm
from .shortTerm import ShortTerm
from modules.utils.dateTime import getDateTime
import json, os

class Memory:
    def __init__(self, memoryPath='memory.json'):
        self.memoryPath = memoryPath;

        self.shortTerm = ShortTerm(memoryPath);
        self.longTerm = LongTerm(memoryPath);

    def writeMemory(self):
        with open(self.memoryPath, 'w') as memoryFile:
            memoryData = {
                'shortTerm': self.shortTerm.memoryData,
                'longTerm': self.longTerm.memoryData
            };

            memoryJson = json.dumps(memoryData);
            memoryFile.write(memoryJson);

    def add(self, key, value):
        time = getDateTime();

        self.shortTerm.add(key, value, time);
        self.longTerm.add(key, value, time);