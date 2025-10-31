import os.path
import shutil
from pathlib import Path

from src.classes.command import Command
from src.classes.exeptions import InvalidCountOfArguments, IsDirectoryError, InvalidFilePath


def unzip(command: Command, file_format="zip") -> None:
    """
    Распаковывает архив в текущую директорию.
    :param command: Команда, которая была написана пользователем.
    :param file_format: Формат архива, который необходимо распаковать, по умолчанию zip.
    :return: Ничего не возвращает.
    """
    if len(command.args) != 1:
        raise InvalidCountOfArguments(command.main_command)
    if os.path.isdir(command.args[0]):
        raise IsDirectoryError(command.main_command, command.args[0])
    if not os.path.exists(command.args[0]):
        raise InvalidFilePath(command.args[0])
    file_name = Path(command.args[0]).stem
    shutil.unpack_archive(command.args[0], format=file_format, extract_dir=file_name)


def untar(command: Command) -> None:
    unzip(command, file_format="gztar")
