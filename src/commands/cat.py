import logging
import os
import pathlib
import sys

from src.command import Command
from src.constants import COMMAND_OUTPUT_LOGGER_NAME
from src.exeptions import InvalidCountOfArguments, InvalidFilePath, IsDirectoryError


def cat(command: Command) -> None:
    """
    Открывает файл, изначально пытается открыть в формате utf-8, если не выходит, выводит содержимое в ISO-8859-1
    :param command: Команда, которая была написана пользователем
    :return: Ничего не возвращает
    """
    if len(command.args) != 1:
        raise InvalidCountOfArguments(command.main_command)
    if not os.path.exists(command.args[0]):
        raise InvalidFilePath(command.args[0])
    if not os.path.isfile(command.args[0]):
        raise IsDirectoryError(command.main_command, command.args[0])
    path = pathlib.Path(command.args[0])
    try:
        logging.getLogger(COMMAND_OUTPUT_LOGGER_NAME).info(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        logging.getLogger(COMMAND_OUTPUT_LOGGER_NAME).info(sys.stdout.buffer.write(path.read_bytes()))
        # sys.stdout.buffer.write(path.read_bytes())
