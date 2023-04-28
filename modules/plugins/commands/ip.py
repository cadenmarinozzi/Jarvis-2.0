import requests

def getIP():
    IP = requests.get("https://api.ipify.org").text;

    return IP;