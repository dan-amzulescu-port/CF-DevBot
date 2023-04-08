from services.dev_bot_svc import DevBotService

if __name__ == '__main__':
    try:
        # if len(sys.argv) < 2 or sys.argv[1] not in DEVBOT_TASKS:
        #     print("Error: Please provide an argument ('dev' or 'merge').")
        #     exit(-1)
        devbot = DevBotService()
        # devbot.run(sys.argv[1])
        devbot.run("merge")
    except Exception as e:
        print(e)
        exit(-1)
    exit(0)
