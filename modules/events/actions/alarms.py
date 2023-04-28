from modules.utils.dateTime import getDateTime, getDeltaTime, getDate, getTime
from simpleSound import play
import json, os

class Alarms:
    def __init__(self, alarmsPath='alarms.json', alarmSoundPath='assets/audio/BackInBlack.mp3'):
        self.alarms = [];

        self.alarmSoundPath = alarmSoundPath;
        self.alarmsPath = alarmsPath;
    
        if (os.path.exists(self.alarmsPath)):
            self.readAlarms();
    
    def readAlarms(self):
        with open(self.alarmsPath, 'r') as alarmsFile:
            alarms = json.load(alarmsFile);
    
            self.alarms = alarms;
    
    def writeAlarms(self):
        with open(self.alarmsPath, 'w') as alarmsFile:
            alarmsJson = json.dumps(self.alarms);
            alarmsFile.write(alarmsJson);

    def playAlarmSound(self):
        play(self.alarmSoundPath);

    def createAlarm(self, args):
        time = args[0];

        if (len(args) > 1):
            date = args[1];

            self.alarms.append({
                'time': time,
                'date': date
            });
        else:
            self.alarms.append({
                'time': time,
                'date': getDate()
            });

        self.writeAlarms();

    def deleteAlarm(self, index):
        del self.alarms[index];

        self.writeAlarms();

    def getAlarm(self, index):
        return self.alarms[index];

    def getAlarms(self):
        return self.alarms;

    def alarmsFunction(self):
        if (len(self.alarms) == 0):
            return;

        for alarm in self.alarms:
            timeDifference = getDeltaTime(getTime(), alarm['time']);
            dateDifference = getDeltaTime(getDate(), alarm['date']);
            print(timeDifference)

            # Play withing 5 seconds of alarm
            if (timeDifference < 5 and timeDifference > 0 and dateDifference == 0):
                self.playAlarmSound();

                self.deleteAlarm(self.alarms.index(alarm));
