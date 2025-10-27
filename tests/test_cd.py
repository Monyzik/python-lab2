import os
import pytest
from src.command import Command
from src.exeptions import InvalidFilePath, InvalidCountOfArguments, IsFileError
from src.constants import COMMANDS

# shell = Shell()
cd = COMMANDS['cd']
start_dir = os.getcwd()


def test_cd():
    cd(Command("cd test_dir"))
    assert os.getcwd() == os.path.join(start_dir, "test_dir")
    cd(Command("cd ."))
    assert os.getcwd() == os.path.join(start_dir, "test_dir")
    cd(Command("cd"))
    assert os.getcwd() == os.path.expanduser("~")
    cd(Command(f"cd {os.path.join(start_dir, 'test_dir')}"))
    assert os.getcwd() == os.path.join(start_dir, "test_dir")
    cd(Command("cd .."))
    assert os.getcwd() == start_dir


def test_cd_invalid_path():
    with pytest.raises(InvalidFilePath):
        cd(Command("cd abacaba"))

def test_cd_invalid_argument_count():
    with pytest.raises(InvalidCountOfArguments):
        cd(Command("cd .. .."))
    with pytest.raises(InvalidCountOfArguments):
        cd(Command("cd . -l abacaba"))

def test_cd_is_file():
    with pytest.raises(IsFileError):
        cd(Command("cd test_dir/test_dir1/test_file1.txt"))
