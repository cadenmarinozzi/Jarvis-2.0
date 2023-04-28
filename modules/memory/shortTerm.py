from modules.web.OpenAI.tokenizer import encode
import json, os

class ShortTerm:
    def __init__(self, memoryPath='memory.json'):
        self.memoryPath = memoryPath;
        self.memoryData = self.readMemory();

    def readMemory(self):
        if (not os.path.exists(self.memoryPath)):
            return [];

        with open(self.memoryPath, 'r') as memoryFile:
            data = json.load(memoryFile)['shortTerm'];

            return data;

    def add(self, key, value, time):
        self.memoryData.append([key, value, time]);

    def getNTokens(self):
        nTokens = 0;

        for i, message in enumerate(self.memoryData):
            nTokens += 4;

            nTokens += len(encode(message[0]));
            nTokens += len(encode(message[1]));

            if (i == 0 or i == 1):
                nTokens += len('system');
            else:
                if (i % 2 == 0):
                    nTokens += len('assistant');
                else:
                    nTokens += len('user');

        nTokens += 2;

        return nTokens;

    def prune(self):
        nTokens = self.getNTokens();

        while (nTokens >= 8192):
            self.memoryData = self.memoryData[1:];

        return;