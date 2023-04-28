from .time import getTime
from .date import getDate
from .internetSpeed import getUploadSpeed, getDownloadSpeed
from .ip import getIP
from .systemSpeed import getCPUSpeed, getRamSpeed
from modules.plugins.functions import aiFunction
from modules.web.OpenAI.OpenAI import createCompletion
from modules.events.events import alarms

commands = {};

commands['time'] = {
    'method': getTime,
    'intext': True
};

commands['date'] = {
    'method': getDate,
    'intext': True
};

commands['upload_speed'] = {
    'method': getUploadSpeed,
    'intext': True
};

commands['download_speed'] = {
    'method': getDownloadSpeed,
    'intext': True
};

commands['ip'] = {
    'method': getIP,
    'intext': True
};

commands['cpu_speed'] = {
    'method': getCPUSpeed,
    'intext': True
};

commands['ram_speed'] = {
    'method': getRamSpeed,
    'intext': True
};

commands['create_alarm'] = {
    'method': alarms.createAlarm,
    'args': ['time (%H:%M:%S AM/PM)', 'date (%d/%m/%Y)'],
};

def runCommand(command, args=[]):
    if command in commands:
        if (args):
            return commands[command]['method'](args);
        else:
            return commands[command]['method']();
    
    description = createCompletion([
        {
            'content': 'You are an AI code function description generator. For the given function name, generate ONLY the description of the function, nothing else.',
            'role': 'system'
        },
        {
            'content': 'Here is an example:\nFunction: time\nDescription: Returns the current time.',
            'role': 'system'
        },
        {
            'content': f'Function: {command}',
            'role': 'user'
        }
    ]);

    return aiFunction(command, description);