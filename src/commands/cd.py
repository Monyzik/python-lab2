import logging
import os

from src.command import Command
from src.constants import FILE_LOGGER_NAME
from src.exeptions import InvalidCountOfArguments, InvalidFilePath, IsFileError


def cd(command: Command) -> None:
    """
    Меняет текущую директорию на новую, если ничего не передано в аргументы, то переводит в ~
    :param command: Команда, которая была написана пользователем
    :return: Ничего не возвращает
    """
    if not command.args:
        os.chdir(os.path.expanduser("~"))
        logging.getLogger(FILE_LOGGER_NAME).info("")
        return
    if len(command.args) > 1:
        raise InvalidCountOfArguments(command.main_command)
    if not os.path.exists(command.args[0]):
        raise InvalidFilePath(command.args[0])
    if os.path.isfile(command.args[0]):
        raise IsFileError(command.main_command, command.args[0])
    os.chdir(command.args[0])
    logging.getLogger(FILE_LOGGER_NAME).info("")
