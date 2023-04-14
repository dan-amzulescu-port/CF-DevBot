import logging
# Set up logging
from subprocess import CompletedProcess


def handle_error(error_message: str, logger: logging.Logger) -> None:
    logging.error(error_message)
    raise Exception(error_message)


def handle_success(message: str, logger: logging.Logger) -> None:
    logger.info(message)


def handle_subprocess_output(output: CompletedProcess, task: str) -> None:
    if output.returncode != 0:
        if output.stderr:
            handle_error(f'{task}: {output.stderr.decode("utf-8")}')
        elif output.stdout:
            handle_error(f'{task}: {output.stdout.decode("utf-8")}')
        else:
            handle_error(f'{task} failed: return code = {output.returncode}')
    else:
        handle_success(f"Successfully executed: {task}")
