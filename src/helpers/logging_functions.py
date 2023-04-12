import logging
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def handle_error(error_message: str) -> None:
    print(error_message)
    logging.error(error_message)
    raise Exception(error_message)


def handle_success(message: str) -> None:
    print(message)
    logging.info(message)
