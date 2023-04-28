from dotenv import load_dotenv
import requests, os
from modules.utils.city import getCity

load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

def getWeatherInCurrentCity():
    city = getCity();

    weatherResponse = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={OPENWEATHERMAP_API_KEY}&q={city}&units=imperial");
    responseJson = weatherResponse.json();
    responseCode = responseJson["cod"];

    if (responseCode == "404"):
        return;
    else:
        main = responseJson["main"];
        wind = responseJson["wind"];
        weather = responseJson["weather"];
        temperature = str(int(main["temp"]));
        airPressure = str(int(main["pressure"]));
        humidity = str(int(main["humidity"]));
        windSpeed = str(int(wind["speed"]));
        description = weather[0]["description"];

        return {
            "temperature": temperature,
            "airPressure": airPressure,
            "humidity": humidity,
            "windSpeed": windSpeed,
            "description": description
        }
    
def getWeatherDescriptionInCurrentCity():
    weather = getWeatherInCurrentCity();

    if (weather == None):
        return;
    else:
        description = weather["description"];

        return description;

def getWeatherTemperatureInCurrentCity():
    weather = getWeatherInCurrentCity();

    if (weather == None):
        return;
    else:
        temperature = weather["temperature"];

        return temperature;