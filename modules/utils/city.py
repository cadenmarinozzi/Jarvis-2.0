import requests, os
from dotenv import load_dotenv

load_dotenv()

IPREGISTRY_API_KEY = os.getenv('IPREGISTRY_API_KEY')

def getCity():
    ipResponse = requests.get(f"https://api.ipregistry.co/?key={IPREGISTRY_API_KEY}");
    responseJson = ipResponse.json();
    city = responseJson["location"]["city"];

    return city;

getCity();