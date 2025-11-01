import os
from unittest.mock import Mock

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.system.command import CommandFromString
from src.system.exeptions import InvalidFilePath, InvalidCountOfArguments
from src.commands.mv import mv


def test_mv(fs: FakeFilesystem, fake_logger_info_call: Mock, fake_project_dir):
    fs.create_dir("test")
    fs.create_file(os.path.join("test", "hello world.txt"), contents="hello world")

    mv(CommandFromString(r"mv 'test/hello world.txt' test/'goodbye world.txt'"))
    assert 'goodbye world.txt' in os.listdir('/test')
    assert 'hello world.txt' not in os.listdir('/test')
    mv(CommandFromString('mv test/ other_test'))
    assert 'other_test' in os.listdir('/')


def test_mv_invalid_file_path():
    with pytest.raises(InvalidFilePath):
        mv(CommandFromString("mv abacaba abacaba"))


def test_mv_invalid_arguments():
    with pytest.raises(InvalidCountOfArguments):
        mv(CommandFromString("mv abacaba"))
