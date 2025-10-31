from typing import Callable

from src.commands.cat import cat
from src.commands.grep import grep
from src.commands.history import history
from src.commands.ls import ls
from src.commands.cd import cd
from src.commands.cp import cp
from src.commands.mv import mv
from src.commands.rm import rm
from src.commands.undo import undo
from src.commands.unzip import unzip, untar
from src.commands.zip import zip_dir, tar
from src.enums.commands import Commands

COMMANDS_FUNCTIONS: dict[str, Callable] = {Commands.cat: cat, Commands.ls: ls, Commands.cd: cd, Commands.cp: cp, Commands.mv: mv,
            Commands.rm: rm, Commands.zip: zip_dir, Commands.unzip: unzip, Commands.tar: tar,
            Commands.untar: untar, Commands.grep: grep, Commands.history: history, Commands.undo: undo}
