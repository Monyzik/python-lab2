import logging
import os
import shutil

from src.command import Command
from src.constants import FILE_LOGGER_NAME
from src.exeptions import InvalidCountOfArguments, IsDirectoryError


def cp(command: Command) -> None:
    if len(command.args) != 2:
        raise InvalidCountOfArguments(command.main_command)
    if 'r' in command.params:
        if os.path.isfile(command.args[0]):
            shutil.copy(command.args[0], command.args[1])
        shutil.copytree(command.args[0], command.args[1], dirs_exist_ok=True)
    else:
        if os.path.isdir(command.args[0]):
            raise IsDirectoryError(command.main_command, command.args[0])
        shutil.copy(command.args[0], command.args[1])
    logging.getLogger(FILE_LOGGER_NAME).info("")
