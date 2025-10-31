import os.path
import shutil

from src.classes.command import Command
from src.classes.exeptions import InvalidCountOfArguments, IsFileError, InvalidFilePath


def zip_dir(command: Command, zip_format="zip") -> None:
    """
    Запаковывает архив в текущую директорию.
    :param command: Команда, которая была написана пользователем.
    :param zip_format: Формат архива, по умолчанию zip.
    :return: Ничего не возвращает.
    """
    if len(command.args) != 2:
        raise InvalidCountOfArguments(command.main_command)
    if os.path.isfile(command.args[0]):
        raise IsFileError(command.main_command, command.args[0])
    if not os.path.exists(command.args[0]):
        raise InvalidFilePath(command.args[0])
    shutil.make_archive(base_dir=command.args[0], format=zip_format, base_name=command.args[1])


def tar(command: Command) -> None:
    zip_dir(command=command, zip_format="gztar")
