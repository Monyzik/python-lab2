import os

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.system.command import CommandFromString
from src.system.exeptions import InvalidFilePath, InvalidCountOfArguments, IsFileError
from src.commands.cd import cd


def test_cd(fs: FakeFilesystem):
    fs.create_dir('test')
    cd(CommandFromString("cd test"))
    assert os.getcwd() == '/test'
    cd(CommandFromString("cd ."))
    assert os.getcwd() == "/test"
    cd(CommandFromString("cd .."))
    assert os.getcwd() == '/'


def test_cd_home_dir():
    cd(CommandFromString("cd"))
    assert os.getcwd() == os.path.expanduser("~")
    cd(CommandFromString("cd ~"))
    assert os.getcwd() == os.path.expanduser("~")


def test_cd_invalid_path():
    with pytest.raises(InvalidFilePath):
        cd(CommandFromString("cd abacaba"))


def test_cd_invalid_argument_count():
    with pytest.raises(InvalidCountOfArguments):
        cd(CommandFromString("cd .. .."))
    with pytest.raises(InvalidCountOfArguments):
        cd(CommandFromString("cd . -l abacaba"))
    with pytest.raises(InvalidCountOfArguments):
        cd(CommandFromString("cd . -l . -l"))


def test_cd_is_file(fs: FakeFilesystem):
    fs.create_dir('test')
    fs.create_file(os.path.join("test", 'test.txt'))
    with pytest.raises(IsFileError):
        cd(CommandFromString("cd test/test.txt"))
