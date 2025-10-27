import logging
import os
import shutil

from src.command import Command
from src.constants import FILE_LOGGER_NAME
from src.exeptions import InvalidCountOfArguments, InvalidFilePath


def mv(command: Command) -> None:
    if len(command.args) != 2:
        raise InvalidCountOfArguments(command.main_command)
    if not os.path.exists(command.args[0]):
        raise InvalidFilePath(command.args[0])
    shutil.move(command.args[0], command.args[1])
    logging.getLogger(FILE_LOGGER_NAME).info("")
