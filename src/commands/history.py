import logging

from src.system.command import Command
from src.common.constants import HISTORY_FILE, COMMAND_OUTPUT_LOGGER_NAME
from src.system.exeptions import InvalidCountOfArguments


def history(command: Command):
    """
    Выводит последние min(n, max_n) команд из .history, где max_n - количество команд в .history
    :param command: Команда, которая была написана пользователем.
    :return: Ничего не возвращает
    """
    if len(command.args) > 1:
        raise InvalidCountOfArguments(command.main_command)
    n = 0
    if command.args:
        n = int(command.args[0])
    history_data: list[str] = []
    with open(HISTORY_FILE, "r") as history_file:
        history_data = list(map(lambda x: x.strip(), history_file.readlines()))
    logging.getLogger(COMMAND_OUTPUT_LOGGER_NAME).info(
        '\n'.join(list(map(lambda x: str(x[0]) + ' ' + x[1], enumerate(history_data, 1)))[-n:]))
