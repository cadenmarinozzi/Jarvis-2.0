import os, json

class Cache:
    def __init__(self, cachePath='cache.json'):
        self.cache = {};
        self.cachePath = cachePath;

    def get(self, key):
        if (key in self.cache):
            return self.cache[key];

    def set(self, key, value):
        self.cache[key] = value;

    def delete(self, key):
        if (key in self.cache):
            del self.cache[key];

    def readCache(self):
        if (not os.path.exists(self.cachePath)):
            return {};

        with open(self.cachePath, 'r') as cacheFile:
            data = json.load(cacheFile);

            return data;

    def writeCache(self):
        with open(self.cachePath, 'w') as cacheFile:
            cacheJson = json.dumps(self.cache);
            cacheFile.write(cacheJson);