import os
from unittest.mock import Mock

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.system.command import CommandFromString
from src.system.exeptions import IsDirectoryError, InvalidCountOfArguments
from src.commands.cp import cp


def test_cp(fs: FakeFilesystem, fake_logger_info_call: Mock, fake_project_dir):
    fs.create_dir("test")
    fs.create_file(os.path.join("test", "hello world.txt"), contents="hello world")
    fs.create_file("okak.txt", contents="Окак")

    cp(CommandFromString(r"cp test/hello\ world.txt test/'goodbye world.txt'"))
    assert 'goodbye world.txt' in os.listdir('/test')
    assert 'hello world.txt' in os.listdir('/test')
    cp(CommandFromString('cp -r test/ other_test'))
    assert 'other_test' in os.listdir('/')


def test_cp_is_dir(fs: FakeFilesystem):
    fs.makedir("test")
    with pytest.raises(IsDirectoryError):
        cp(CommandFromString("cp test test2"))


def test_cp_invalid_arguments():
    with pytest.raises(InvalidCountOfArguments):
        cp(CommandFromString("cp abacaba"))
