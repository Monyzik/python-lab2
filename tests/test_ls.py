import os
from datetime import datetime
from unittest.mock import Mock

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.classes.command import CommandFromString
from src.classes.exeptions import IsFileError, InvalidFilePath
from src.commands.ls import ls


def test_ls(fs: FakeFilesystem, fake_logger_info_call: Mock):
    fs.create_dir("test")
    fs.create_file(os.path.join("test", "hello world.txt"), contents="hello world")
    fs.create_file("okak.txt", contents="Окак")

    ls(CommandFromString("ls"))
    out = fake_logger_info_call.call_args.args[0]
    assert 'test' in out
    assert "okak.txt" in out
    ls(CommandFromString('ls test/ -l'))
    out = fake_logger_info_call.call_args.args[0]
    assert 'hello world.txt' in out
    assert "-rw-r--r--" in out
    assert str(datetime.now().year) in out


def test_permissions_in_files(fs: FakeFilesystem, fake_logger_error_call: Mock):
    fs.create_file("hello world.txt", contents="hello world")
    fs.chmod("hello world.txt", 0)
    ls(CommandFromString('ls -l /'))
    out = fake_logger_error_call.call_args.args[0]
    assert "Недостаточно прав доступа" in str(out)


def test_ls_is_file(fs: FakeFilesystem):
    fs.create_file("test.txt")
    with pytest.raises(IsFileError):
        ls(CommandFromString("ls test.txt"))


def test_ls_invalid_path():
    with pytest.raises(InvalidFilePath):
        ls(CommandFromString("ls abacaba"))
