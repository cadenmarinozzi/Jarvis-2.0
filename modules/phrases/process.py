from .commands.commands import runCommand
from .phrases import phrases
import re

commandRegex = re.compile(r'<.+?>');

def processPhrase(text):
    commands = commandRegex.findall(text);

    for commandText in commands:
        command = commandText[1:-1];
        result = runCommand(command);

        if (result):
            text = text.replace(commandText, result);

    return text;

def runPhrase(phrase):
    return processPhrase(phrases[phrase]);