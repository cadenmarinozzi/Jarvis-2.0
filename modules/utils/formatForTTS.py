def formatForTTS(text):
    text = text.replace('\n', ' ');
    text = text.replace('\t', ' ');
    text = text.replace('\r', ' ');
    text = text.replace('\\', '');
    text = text.replace('<', '');
    text = text.replace('>', '');
    text = text.replace('"', ' ');
    text = text.replace('\'', ' ');

    return text;