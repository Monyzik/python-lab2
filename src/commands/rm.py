import os
import shutil
from datetime import datetime
from pathlib import Path

from src.classes.command import Command
from src.common.constants import TRASH_DIR
from src.classes.exeptions import InvalidCountOfArguments, InvalidFilePath, IsDirectoryError, ImpossibleToDelete
from src.classes.json_logger import JsonLogger


def rm(command: Command, ask: bool = True, undo_logging: bool = True) -> None:
    """
    Удаляет файл, если передан параметр -r, то может рекурсивно удалить директорию, не может удалять директории: './', '../', '/'.
    :param command: Команда, которая была написана пользователем.
    :param ask: Флаг, который отвечает за необходимость подтверждения у пользователя об удалении файла/директории.
    :param undo_logging: Флаг, который отвечает за необходимость логирования для undo.
    :return: Ничего не возвращает.
    """
    if len(command.args) != 1:
        raise InvalidCountOfArguments(command.main_command)
    if not os.path.exists(command.args[0]):
        raise InvalidFilePath(command.args[0])
    if command.args[0] in ['.', '..', '/']:
        raise ImpossibleToDelete(command.args[0])
    if os.path.isdir(command.args[0]) and 'r' not in command.params:
        raise IsDirectoryError(command.main_command, command.args[0])
    if ask:
        print(f"Вы уверенны, что хотите удалить {command.args[0]} (y/n)")
        answer = input()
        if answer.lower().strip() not in ["y", "yes", "да"]:
            return
    if undo_logging:
        base_name = Path(command.args[0]).stem
        suffix = Path(command.args[0]).suffix
        trash_path = os.path.join(TRASH_DIR, base_name + '_' + str(datetime.now().timestamp()) + suffix)
        if os.path.isfile(command.args[0]):
            shutil.copy(command.args[0], trash_path)
        else:
            shutil.copytree(command.args[0], trash_path)
        JsonLogger(command.main_command, command.args[0], trash_path, command.params).write()

    if os.path.isfile(command.args[0]):
        os.remove(command.args[0])
    else:
        shutil.rmtree(command.args[0])
