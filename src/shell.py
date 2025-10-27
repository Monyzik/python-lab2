import logging
import os

from src.command import Command
from src.constants import COMMANDS, COMMAND_INPUT_LOGGER_NAME, ERROR_LOGGER_NAME
from src.exeptions import InvalidCommandName


class Shell:
    def __init__(self, cur_dir=None):
        if cur_dir and os.path.exists(os.path.expanduser(cur_dir)):
            os.chdir(os.path.expanduser(cur_dir))
        self.cur_dir = cur_dir
        # self.command_logger = logging.getLogger("command_logger")

    def complete_command(self, command: str):
        error_logger = logging.getLogger(ERROR_LOGGER_NAME)
        try:
            command = Command(1, command)
        except ValueError as exception:
            error_logger.error(exception)
            return
        logging.getLogger(COMMAND_INPUT_LOGGER_NAME).info(command)
        if command.main_command not in COMMANDS:
            error_logger.error(InvalidCommandName(command.main_command))
            return
        try:
            COMMANDS[command.main_command](command)
        except Exception as exception:
            error_logger.error(f"{exception.__class__.__name__}: {exception}")

    def get_cur_dir(self):
        return self.cur_dir
