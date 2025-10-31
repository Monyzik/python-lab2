import os
import shutil

from src.classes.command import Command
from src.classes.exeptions import InvalidCountOfArguments, IsDirectoryError
from src.classes.json_logger import JsonLogger


def cp(command: Command, undo_logging: bool = True) -> None:
    """
    Копирует файл или директорию, если передан флаг -r.
    :param command: Команда, которая была написана пользователем.
    :param undo_logging: Флаг, который отвечает за необходимость логирования для undo.
    :return: Ничего не возвращает.
    """
    if len(command.args) != 2:
        raise InvalidCountOfArguments(command.main_command)
    if 'r' not in command.params and os.path.isdir(command.args[0]):
        raise IsDirectoryError(command.main_command, command.args[0])
    if os.path.isfile(command.args[0]):
        shutil.copy(command.args[0], command.args[1])
    else:
        shutil.copytree(command.args[0], command.args[1], dirs_exist_ok=True)
    if undo_logging:
        JsonLogger(command.main_command, command.args[0], command.args[1], command.params).write()
