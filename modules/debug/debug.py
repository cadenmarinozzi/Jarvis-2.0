from modules.config.config import getConfig
import logging
from rich.logging import RichHandler

config = getConfig("config.json")

if (config['debugging']):
    FORMAT = "%(message)s"
    logging.basicConfig(
        level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
    )
    log = logging.getLogger("rich")

def debugMessage(message):
    if (config['debugging']):
        log.info(message)