from datetime import datetime

def getDateTime():
    now = datetime.now();
    time = now.strftime("%d/%m/%Y %I:%M:%S %p");
    
    return time;

def getDate():
    now = datetime.now();
    time = now.strftime("%d/%m/%Y");
    
    return time;

def getTime():
    now = datetime.now();
    time = now.strftime("%I:%M:%S %p");
    
    return time;

def getDeltaTime(time1, time2):
    dateTime1 = datetime.strptime(time1, "%I:%M:%S %p")
    dateTime2 = datetime.strptime(time2, "%I:%M:%S %p")

    deltaTime = dateTime2 - dateTime1

    return deltaTime.total_seconds();

def getDeltaDate(date1, date2):
    dateTime1 = datetime.strptime(date1, "%d/%m/%Y")
    dateTime2 = datetime.strptime(date2, "%d/%m/%Y")

    deltaTime = dateTime2 - dateTime1

    return abs(deltaTime.days);