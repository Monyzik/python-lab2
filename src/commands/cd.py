import os

from src.system.command import Command
from src.system.exeptions import InvalidCountOfArguments, InvalidFilePath, IsFileError


def cd(command: Command) -> None:
    """
    Меняет текущую директорию на новую, если ничего не передано в аргументы, то переводит в ~.
    :param command: Команда, которая была написана пользователем.
    :return: Ничего не возвращает.
    """
    if not command.args:
        os.chdir(os.path.expanduser("~"))
        return
    if len(command.args) > 1:
        raise InvalidCountOfArguments(command.main_command)
    if not os.path.exists(command.args[0]):
        raise InvalidFilePath(command.args[0])
    if os.path.isfile(command.args[0]):
        raise IsFileError(command.main_command, command.args[0])
    os.chdir(command.args[0])
