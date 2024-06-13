import logging
import sys

from constants import DEVBOT_TASKS
from helpers.logging_functions import handle_error
from services.dev_bot_svc import DevBotService

log_level = logging.DEBUG
logging.basicConfig(level=log_level)  # Set logging level to DEBUG
logger = logging.getLogger(__name__)  # Create a logger for the current module

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2 or sys.argv[1] not in DEVBOT_TASKS:
            handle_error("Please provide an argument ('dev', 'merge_prs' or 'clean').", logger)
        devbot = DevBotService()
        devbot.run(sys.argv[1])
    except Exception as e:
        logger.critical("Error: ", e)
        exit(-1)
    exit(0)
