from modules.web.OpenAI.OpenAI import createCompletion
from modules.utils.dateTime import getDateTime
from modules.plugins.commands.commands import commands

def processQuery(query, state):
    # if (state.cache.get(query)):
    #     return state.cache.get(query);

    shortTermMemoryData = state.memory.shortTerm.memoryData;

    name = state.config['name'];
    messages = [
        {
            'content': f'You are an AI assistant. Your name is {name}. You are helpful and informative. You should refer to your user as "sir" as much as possible. Your responses should be short and concise.',
            'role': 'system'
        }
    ];

    commandsList = '';

    for commandName, command in commands.items():
        if ('intext' in command):
            commandsList += f'<{commandName}_intext>, ';
        else:
            if ('args' in command):
                argsList = ', '.join(command['args']);
                commandsList += f'<{commandName}[{argsList}]>, ';
            
                continue;
            
            commandsList += f'<{commandName}>, ';

    messages.append({
        'content': f'Here is a list of commands you can use: {commandsList}.\nAn example of how to use these commands would be like this: User: "Jarvis, what is the time?", Assistant: "It is <time_intext>."',
        'role': 'system'
    });

    messages.append({
        'content': f'If the user request requires a command that does not exist, for example, "Jarvis, what is the weather?", you should still respond with the command, as if it exists. For example, "It is <weather_intext>."',
        'role': 'system'
    });

    for message in shortTermMemoryData:     
        time = message[2];
        userMessage = message[0];

        messages.append({
            'content': f'It is: {time}. {userMessage}',
            'role': 'user'
        });

        messages.append({
            'content': message[1],
            'role': 'assistant'
        });

    time = getDateTime();

    messages.append({
        'content': query, 
        'role': 'user'
    });
        
    response = createCompletion(messages, state=state);

    return response;