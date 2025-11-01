import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.system.command import CommandFromString
from src.system.exeptions import InvalidCountOfArguments
from src.system.shell import Shell
from src.commands.history import history
from src.common.set_default_logging_config import set_default_logging_config


def test_history(fs: FakeFilesystem, fake_project_dir, capsys):
    set_default_logging_config()
    shell = Shell("/")
    shell.complete_command("ls -la")
    shell.complete_command("cp .history history1")

    shell.complete_command("history 10")
    out, err = capsys.readouterr()
    assert '3 history' in out
    history(CommandFromString("history"))
    out, err = capsys.readouterr()
    assert '3 history' in out
    assert '2 cp .history history1' in out
    assert "1 ls -la" in out


def test_history_invalid_arguments():
    with pytest.raises(InvalidCountOfArguments):
        history(CommandFromString("history abacaba abacaba abacaba"))
