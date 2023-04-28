from datetime import datetime

def getDate():
    now = datetime.now();
    date = now.strftime("%d/%m/%Y");
    
    return date;