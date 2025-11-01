import os

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.system.command import CommandFromString
from src.system.exeptions import InvalidCountOfArguments, NoCommandToUndo
from src.system.shell import Shell
from src.commands.rm import rm
from src.commands.undo import undo
from src.common.set_default_logging_config import set_default_logging_config


def test_undo(fs: FakeFilesystem, fake_project_dir):
    set_default_logging_config()
    shell = Shell("/")
    shell.complete_command("cp .history history1")
    shell.complete_command("mv history1 history_moved")
    rm(CommandFromString("rm history_moved"), ask=False)

    assert "history_moved" not in os.listdir("/")
    shell.complete_command("undo")
    assert "history_moved" in os.listdir("/")
    shell.complete_command("undo")
    assert "history1" in os.listdir("/")
    shell.complete_command("undo")
    assert "history1" not in os.listdir("/")
    with pytest.raises(NoCommandToUndo):
        undo(CommandFromString("undo"))


def test_undo_invalid_arguments():
    with pytest.raises(InvalidCountOfArguments):
        undo(CommandFromString("undo abacaba"))


def test_undo_empty_history(fs: FakeFilesystem, fake_project_dir):
    with pytest.raises(NoCommandToUndo):
        undo(CommandFromString("undo"))
