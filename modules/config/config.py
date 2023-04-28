import json

def getConfig(configPath):
    with open(configPath, 'r') as configFile:
        config = json.load(configFile);

    return config;