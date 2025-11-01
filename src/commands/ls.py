import logging
import os
import stat
import time

from tabulate import tabulate # type: ignore

from src.system.command import Command
from src.common.constants import COMMAND_OUTPUT_LOGGER_NAME, ERROR_LOGGER_NAME
from src.system.exeptions import InvalidAccessForFile, InvalidFilePath, IsFileError


def ls(command: Command) -> None:
    """
    Выводит информацию о текущем каталоге, либо о каталогах, которые были переданы в аргументы функции.
    При параметре -l выводит информацию в виде: [название файла] [права доступа] [размер в байтах] [дата изменения фйла]
    :param command: Команда, которая была написана пользователем
    :return: Ничего не возвращает
    """
    result: list[list[str]] = list()
    if command.args:
        for path in command.args:
            if not os.path.exists(path):
                raise InvalidFilePath(path)
            if os.path.isfile(path):
                raise IsFileError(command.main_command, path)
            result.append([os.path.join(path, file) for file in os.listdir(path)])
    else:
        result.append(os.listdir(os.getcwd()))

    output_logger = logging.getLogger(COMMAND_OUTPUT_LOGGER_NAME)
    output = []
    for paths in result:
        for item in paths:
            file_name = os.path.basename(item)
            if 'l' in command.params:
                if not os.access(item, os.R_OK):
                    logging.getLogger(ERROR_LOGGER_NAME).error(InvalidAccessForFile(item))
                    continue
                file_info = os.stat(item)
                file_size = file_info.st_size
                last_modified = time.ctime(file_info.st_mtime)
                mode = file_info.st_mode
                permissions_string = stat.filemode(mode)
                output.append([file_name, permissions_string, file_size, last_modified])
            else:
                output.append([file_name])
    output_logger.info(tabulate(output))
