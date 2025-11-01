import json
import os

from src.system.command import Command
from src.commands.cp import cp
from src.commands.mv import mv
from src.commands.rm import rm
from src.common.constants import UNDO_HISTORY_FILE
from src.system.exeptions import InvalidCountOfArguments, NoCommandToUndo
from src.system.commands import Commands


def undo(command: Command):
    """
    Отменяет последнюю из команд: cp, rm, mv.
    :param command: Команда, которая была написана пользователем.
    :return: Ничего не возвращает.
    """
    if command.args:
        raise InvalidCountOfArguments(command.main_command)
    if not os.path.exists(UNDO_HISTORY_FILE):
        raise NoCommandToUndo()
    with open(UNDO_HISTORY_FILE, 'r') as file:
        lines = file.readlines()
        if not lines:
            raise NoCommandToUndo()
        command_last = json.loads(lines.pop())
    with open(UNDO_HISTORY_FILE, 'w') as file:
        file.writelines(lines)

    function = command_last['function']
    to_path = command_last['to_path']
    from_path = command_last['from_path']
    params = command_last['params']
    if function == Commands.mv:
        mv(Command(Commands.mv, [to_path, from_path], params), undo_logging=False)
    elif function == Commands.cp:
        rm(Command(Commands.cp, [to_path], params), ask=False, undo_logging=False)
    elif function == Commands.rm:
        cp(Command(Commands.cp, [to_path, from_path], params), undo_logging=False)
        rm(Command(Commands.rm, [to_path], params), ask=False, undo_logging=False)
