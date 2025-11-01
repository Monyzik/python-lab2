import os
import shutil

from src.system.command import Command
from src.system.exeptions import InvalidCountOfArguments, InvalidFilePath
from src.system.json_logger import JsonLogger


def mv(command: Command, undo_logging: bool = True) -> None:
    """
    Перемещает файл/директорию, если передано новое название файла/директории, то переименовывает его/её.
    :param command: Команда, которая была написана пользователем.
    :param undo_logging: Флаг, который отвечает за необходимость логирования для undo.
    :return: Ничего не возвращает.
    """
    if len(command.args) != 2:
        raise InvalidCountOfArguments(command.main_command)
    if not os.path.exists(command.args[0]):
        raise InvalidFilePath(command.args[0])
    shutil.move(command.args[0], command.args[1])
    if undo_logging:
        JsonLogger(command.main_command, command.args[0], command.args[1], command.params).write()
