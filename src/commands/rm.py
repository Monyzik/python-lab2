import logging
import os
import shutil

from src.command import Command
from src.constants import FILE_LOGGER_NAME
from src.exeptions import InvalidCountOfArguments, InvalidFilePath, IsDirectoryError, ImpossibleToDelete


def rm(command: Command) -> None:
    if len(command.args) != 1:
        raise InvalidCountOfArguments(command.main_command)
    if not os.path.exists(command.args[0]):
        raise InvalidFilePath(command.args[0])
    if command.args[0] in ['.', '..', '/']:
        raise ImpossibleToDelete(command.args[0])
    if os.path.isdir(command.args[0]) and 'r' not in command.params:
        raise IsDirectoryError(command.main_command, command.args[0])
    print(f"Вы уверенны, что хотите удалить {command.args[0]} (y/n)")
    answer = input()
    if answer.lower().strip() not in ["y", "yes", "да"]:
        return
    if os.path.isfile(command.args[0]):
        os.remove(command.args[0])
    else:
        shutil.rmtree(command.args[0])
    logging.getLogger(FILE_LOGGER_NAME).info("")
