from .actions.alarms import Alarms
from .actions.wakeup import WakeupAlarm
from modules.config.config import getConfig

config = getConfig('config.json');

alarms = Alarms();
wakeupAlarm = WakeupAlarm(config['wakeup-time']);

def beginEventLoop():
    try:
        while True:
            alarms.alarmsFunction();
            wakeupAlarm.alarmsFunction();

    except (KeyboardInterrupt, SystemExit):
        pass;

    alarms.writeAlarms();