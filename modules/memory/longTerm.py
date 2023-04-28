from modules.web.OpenAI.OpenAI import createEmbedding, getSimilarity
import pandas as pd
import numpy as np
import json, os

class LongTerm:
    def __init__(self, memoryPath='memory.json'):
        self.memoryPath = memoryPath;
        self.memoryData = self.readMemory();

    def writeMemory(self):
        with open(self.memoryPath, 'w') as memoryFile:
            memoryJson = json.dumps(self.memoryData);
            memoryFile.write(memoryJson);

    def readMemory(self):
        if (not os.path.exists(self.memoryPath)):
            return [];

        with open(self.memoryPath, 'r') as memoryFile:
            data = json.load(memoryFile)['longTerm'];

            return data;

    def add(self, key, value, time):
        self.memoryData.append([key, value, time]);

    def getSearchData(self):
        """ Create a set of memory data in the format:
        [
            ['', 'User1'],
            ['Bot1', 'User2'],
            ['Bot2', '']
        ]

        From memory data in the format:
        [
            ['User1', 'Bot1', 'time'],
            ['Bot2', 'User2', 'time']
        ]
        """

        searchData = [];

        for i in range(len(self.memoryData)):
            item = self.memoryData[i];

            if (i == 0):
                searchData.append(['', item[0]]);
            else:
                searchData.append([self.memoryData[i - 1][1], item[0]]);

            if (i == len(self.memoryData) - 1):
                searchData.append([item[1], '']);

        return searchData;

    def search(self, query):
        searchData = self.getSearchData();
        df = pd.DataFrame(searchData, columns=['response', 'key']);

        embeddings = [];

        for item in searchData:
            key = item[0];
            value = item[1];

            embedding = createEmbedding(f'{key},{value}');
            embeddings.append(embedding);

        df['embedding'] = embeddings;

        inputEmbedding = createEmbedding(query);

        df['similarity'] = df['embedding'].apply(lambda x: getSimilarity(x, inputEmbedding));

        highestSimilarity = df['similarity'].max();
        highestItem = df.loc[df['similarity'] == highestSimilarity];
        
        return (highestItem, highestSimilarity);