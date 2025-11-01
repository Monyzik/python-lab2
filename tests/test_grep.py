import os
from unittest.mock import Mock

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.system.command import CommandFromString
from src.system.exeptions import InvalidFilePath, InvalidCountOfArguments, IsDirectoryError
from src.commands.grep import grep


def test_grep(fs: FakeFilesystem, fake_logger_info_call: Mock):
    fs.create_dir("test")
    fs.create_file("not interesting.txt", contents="blablabla")
    fs.create_file(os.path.join("test", "hello world.txt"), contents="hello world")
    fs.create_file("okak.txt", contents="hi World")

    grep(CommandFromString("grep 'h*ld' test/hello\ world.txt"))
    out = fake_logger_info_call.call_args.args[0]
    assert 'hello world.txt' in out
    assert "hello world" in out
    grep(CommandFromString("grep 'h*ld' ./ -r"))
    out = fake_logger_info_call.call_args.args[0]
    assert 'hello world.txt' in out
    assert "hello world" in out
    assert 'okak.txt' in out
    assert "hi World" in out
    grep(CommandFromString("grep 'h*World' ./ -ri"))
    out = fake_logger_info_call.call_args.args[0]
    assert 'hello world.txt' in out
    assert "hello world" in out
    assert 'okak.txt' in out
    assert "hi World" in out


def test_grep_invalid_arguments():
    with pytest.raises(InvalidCountOfArguments):
        grep(CommandFromString("grep abacaba abacaba abacaba"))


def test_grep_is_dir(fs: FakeFilesystem):
    fs.makedir("test")
    with pytest.raises(IsDirectoryError):
        grep(CommandFromString("grep 'hello' ./"))


def test_grep_invalid_path():
    with pytest.raises(InvalidFilePath):
        grep(CommandFromString("grep 'hello' abacaba"))
