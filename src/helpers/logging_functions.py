import logging
# Set up logging
from subprocess import CompletedProcess

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def handle_error(error_message: str) -> None:
    print(error_message)
    logging.error(error_message)
    raise Exception(error_message)


def handle_success(message: str) -> None:
    print(message)
    logging.info(message)


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
