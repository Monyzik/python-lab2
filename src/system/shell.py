import logging
import os

from src.system.command import CommandFromString
from src.system.exeptions import InvalidCommandName, InvalidParameters
from src.common.constants import COMMAND_INPUT_LOGGER_NAME, ERROR_LOGGER_NAME, FILE_LOGGER_NAME
from src.common.register import COMMANDS_FUNCTIONS, COMMANDS_PARAMS


class Shell:
    def __init__(self, current_dir=None):
        """
        Инициализирует командную строку.
        :param current_dir: Может принимать начальную директорию.
        """
        if current_dir and os.path.exists(os.path.expanduser(current_dir)):
            os.chdir(os.path.expanduser(current_dir))
        self.cur_dir = os.getcwd()
        self.error_logger = logging.getLogger(ERROR_LOGGER_NAME)
        self.file_logger = logging.getLogger(FILE_LOGGER_NAME)
        self.command_input_logger = logging.getLogger(COMMAND_INPUT_LOGGER_NAME)

    def complete_command(self, command_str: str) -> None:
        """
        Выполняет команду, введенную пользователем.
        :param command_str: Команда введенная пользователем.
        :return: Ничего не возвращает.
        """
        try:
            command = CommandFromString(command_str)
        except ValueError as exception:
            self.error_logger.error(exception)
            return
        self.command_input_logger.info(command)
        if command.main_command not in COMMANDS_FUNCTIONS:
            self.error_logger.error(InvalidCommandName(command.main_command))
            return
        for param in command.params:
            if param not in COMMANDS_PARAMS[command.main_command]:
                self.error_logger.error(InvalidParameters(command.main_command, param))
                return
        try:
            COMMANDS_FUNCTIONS[command.main_command](command)
            self.file_logger.info("Done successfully")
        except Exception as exception:
            self.error_logger.error(f"{exception.__class__.__name__}: {exception}")
        self.update_current_dir()

    def update_current_dir(self):
        if not os.path.exists(self.cur_dir):
            os.chdir(os.path.expanduser('~'))
        self.cur_dir = os.getcwd()

    def get_cur_dir(self):
        return self.cur_dir
