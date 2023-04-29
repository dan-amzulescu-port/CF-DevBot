from datetime import datetime


def timestamp() -> str:
    now = datetime.now()
    return now.strftime('%m%d%H%M%S')
