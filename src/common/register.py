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
from src.system.commands import Commands

COMMANDS_FUNCTIONS: dict[str, Callable] = {Commands.cat: cat,
                                           Commands.ls: ls,
                                           Commands.cd: cd,
                                           Commands.cp: cp,
                                           Commands.mv: mv,
                                           Commands.rm: rm,
                                           Commands.zip: zip_dir,
                                           Commands.unzip: unzip,
                                           Commands.tar: tar,
                                           Commands.untar: untar,
                                           Commands.grep: grep,
                                           Commands.history: history,
                                           Commands.undo: undo}

COMMANDS_PARAMS: dict[str, list[str]] = {Commands.cat: [],
                                         Commands.ls: ['l'],
                                         Commands.cd: [],
                                         Commands.cp: ['r'],
                                         Commands.mv: [],
                                         Commands.rm: ['r'],
                                         Commands.zip: [],
                                         Commands.unzip: [],
                                         Commands.tar: [],
                                         Commands.untar: [],
                                         Commands.grep: ['i', 'r'],
                                         Commands.history: [],
                                         Commands.undo: []}
