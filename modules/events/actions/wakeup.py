from modules.utils.dateTime import getDateTime, getDeltaTime, getDate, getTime
from simpleSound import play
from modules.speech.textToSpeech.textToSpeech import createAndStreamTextToSpeech, createAndPlayTextToSpeechWav
from modules.phrases.process import runPhrase
import time

from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1";

import pygame

pygame.init();
pygame.mixer.init();

class WakeupAlarm:
    def __init__(self, alarmTime, alarmSoundPath='assets/audio/ShouldIStayOrShouldIGo.mp3'):
        self.alarmSoundPath = alarmSoundPath;
        self.alarmTime = alarmTime;
        self.playedAlarm = False;

    def playAlarmSound(self):
        pygame.mixer.music.load(self.alarmSoundPath);
        pygame.mixer.music.play();

        time.sleep(10);

        pygame.mixer.music.fadeout(5000);
    
        createAndStreamTextToSpeech(runPhrase('wakeup'));

    def alarmsFunction(self):
        timeDifference = getDeltaTime(getTime(), self.alarmTime);

        # Play withing 5 seconds of alarm
        if (timeDifference < 5 and timeDifference > 0 and not self.playedAlarm):
            self.playAlarmSound();
            self.playedAlarm = True;
        elif (timeDifference > 5):
            self.playedAlarm = False;