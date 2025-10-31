import logging
import os
import re

from src.classes.command import Command
from src.common.constants import COMMAND_OUTPUT_LOGGER_NAME
from src.classes.exeptions import InvalidCountOfArguments, IsDirectoryError


def grep(command: Command) -> None:
    """
    Ищет строки, которые соответствуют паттерну. При флаге -r рекурсивно перебирает все файлы в каталоге.
    При флаге -i не учитывает регистр при поиске.
    :param command: Команда, которая была написана пользователем.
    :return: Ничего не возвращает
    """
    if len(command.args) != 2:
        raise InvalidCountOfArguments(command.main_command)
    if 'r' not in command.params and os.path.isdir(command.args[1]):
        raise IsDirectoryError(command.main_command, command.args[1])
    ignore_case = False
    if 'i' in command.params:
        ignore_case = True
    answer = ""
    if os.path.isdir(command.args[1]):
        for root, dirs, files in os.walk(command.args[1]):
            for file in files:
                result = find_in_file(command.args[0], str(os.path.join(root, file)), ignore_case=ignore_case)
                if not result:
                    continue
                answer += f"----{file}----\n"
                for number, line in result:
                    answer += f"{number}: {line}\n"
    else:
        result = find_in_file(command.args[0], command.args[1], ignore_case=ignore_case)
        if result:
            answer += f"----{command.args[1]}----\n"
            for number, line in result:
                answer += f"{number}: {line}\n"

    logging.getLogger(COMMAND_OUTPUT_LOGGER_NAME).info(answer)


def find_in_file(pattern: str, path: str, ignore_case: bool = False) -> list[tuple[int, str]]:
    """
    Ищет в файле строки, которые удовлетворяют паттерну.
    :param pattern: Паттерн, который должен содержаться в строке.
    :param path: Путь до файла в котором происходит поиск.
    :param ignore_case: Значение, определяющее будет ли учитываться регистр при поиске.
    :return: Возвращает пустой массив, если ничего не найдено, либо невозможно открыть файл,
     или массив с кортежами, где первое значение это номер строки, а второе значение это сама строка
    """
    lines = []
    try:
        with open(path) as file:
            lines = file.readlines()
    except (UnicodeError, PermissionError):
        return []
    result = []
    for number, line in enumerate(lines, 1):
        if re.search(pattern=pattern, string=line, flags=re.IGNORECASE * ignore_case):
            result.append((number, line.strip()))
    return result
