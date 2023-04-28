from .time import getTime
from .weather import getWeatherDescriptionInCurrentCity, getWeatherTemperatureInCurrentCity

commands = {};

commands['time'] = {
    'method': getTime,
};

commands['weather_description'] = {
    'method': getWeatherDescriptionInCurrentCity,
};

commands['weather_temperature'] = {
    'method': getWeatherTemperatureInCurrentCity,
};

def runCommand(command):
    return commands[command]['method']();