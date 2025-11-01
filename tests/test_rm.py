import os
from unittest.mock import Mock

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.system.command import CommandFromString
from src.system.exeptions import InvalidFilePath, IsDirectoryError, InvalidCountOfArguments, ImpossibleToDelete
from src.commands.rm import rm


def test_rm(fs: FakeFilesystem, fake_logger_info_call: Mock, fake_project_dir):
    fs.create_dir("test")
    fs.create_file(os.path.join("test", "hello world.txt"), contents="hello world")
    os.chdir("test/")
    rm(CommandFromString(r"rm '/test/' -r"), ask=False)
    assert 'test' not in os.listdir('/')
    fs.create_file('test.txt')
    rm(CommandFromString('rm test.txt'), ask=False)
    assert 'test.txt' not in os.listdir('/')


def test_rm_invalid_file_path():
    with pytest.raises(InvalidFilePath):
        rm(CommandFromString("rm abacaba"))


def test_rm_impossible_to_delete():
    with pytest.raises(ImpossibleToDelete):
        rm(CommandFromString("rm .."))
    with pytest.raises(ImpossibleToDelete):
        rm(CommandFromString("rm /"))
    with pytest.raises(ImpossibleToDelete):
        rm(CommandFromString("rm ."))


def test_rm_is_dir(fs: FakeFilesystem):
    fs.create_dir("test")
    with pytest.raises(IsDirectoryError):
        rm(CommandFromString("rm test"))


def test_rm_invalid_arguments():
    with pytest.raises(InvalidCountOfArguments):
        rm(CommandFromString("rm abacaba abacaba"))
