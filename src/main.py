import sys

from constants import DEVBOT_TASKS
from helpers.logging_functions import handle_error
from services.dev_bot_svc import DevBotService

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2 or sys.argv[1] not in DEVBOT_TASKS:
            handle_error("Please provide an argument ('dev' or 'merge').")
        devbot = DevBotService()
        devbot.run(sys.argv[1])
    except Exception as e:
        print("Error: ", e)
        exit(-1)
    exit(0)
