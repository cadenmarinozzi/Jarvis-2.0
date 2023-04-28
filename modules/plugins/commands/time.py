from datetime import datetime

def getTime():
    now = datetime.now();
    time = now.strftime("%I:%M %p");
    
    return time;