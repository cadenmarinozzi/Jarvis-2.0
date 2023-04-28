from .commands.commands import runCommand
import re

intextCommandRegex = re.compile(r'<.+?_intext>');
commandRegex = re.compile(r'<.+?\[.+?\]>');
argsRegex = re.compile(r'\[.+?\]');

def pluginText(text):
    commands = intextCommandRegex.findall(text);

    if (not commands):
        commands = commandRegex.findall(text);

        for commandText in commands:
            commandText = commandText[1:-1];

            args = argsRegex.findall(commandText);

            if (args):
                args = args[0][1:-1].split(', ');
                command = commandText.split('[')[0];

                result = runCommand(command, args);

                if (result):
                    text = text.replace(commandText, result);

            if (result):
                text = text.replace(commandText, result);
    
        return;

    for commandText in commands:
        command = commandText[1:-1];
        result = runCommand(command.replace('_intext', ''));

        if (result):
            text = text.replace(commandText, result);

    return text;