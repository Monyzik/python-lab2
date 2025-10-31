import logging
import sys

from src.common.constants import DATAFORMAT, LOG_FILE, COMMAND_INPUT_LOGGER_NAME, ERROR_LOGGER_NAME, \
    COMMAND_OUTPUT_LOGGER_NAME, HISTORY_FILE, FILE_LOGGER_NAME


def set_default_logging_config():
    """
    Устанавливает настройки логгера
    :return: Ничего не возвращает
    """
    command_input_logger = logging.getLogger(COMMAND_INPUT_LOGGER_NAME)
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(logging.Formatter("[%(asctime)s] %(message)s", datefmt=DATAFORMAT))
    command_input_logger.addHandler(file_handler)
    history_file_handler = logging.FileHandler(HISTORY_FILE)
    history_file_handler.setFormatter(logging.Formatter("%(message)s"))
    command_input_logger.addHandler(history_file_handler)
    command_input_logger.setLevel(logging.INFO)

    error_logger = logging.getLogger(ERROR_LOGGER_NAME)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter("%(message)s"))
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", datefmt=DATAFORMAT))
    error_logger.addHandler(file_handler)
    error_logger.addHandler(stream_handler)
    error_logger.setLevel(logging.ERROR)

    command_output_logger = logging.getLogger(COMMAND_OUTPUT_LOGGER_NAME)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter("%(message)s"))
    command_output_logger.addHandler(stream_handler)
    command_output_logger.setLevel(logging.INFO)

    file_logger = logging.getLogger(FILE_LOGGER_NAME)
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", datefmt=DATAFORMAT))
    file_logger.addHandler(file_handler)
    file_logger.setLevel(logging.INFO)
