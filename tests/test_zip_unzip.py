import os
from unittest.mock import Mock

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.classes.command import CommandFromString
from src.classes.exeptions import InvalidCountOfArguments, IsFileError, InvalidFilePath, IsDirectoryError
from src.commands.unzip import unzip, untar
from src.commands.zip import zip_dir, tar


def test_zip(fs: FakeFilesystem, fake_logger_info_call: Mock, fake_project_dir):
    fs.create_dir("test")
    fs.create_file(os.path.join("test", "hello world.txt"), contents="hello world")
    zip_dir(CommandFromString(r"zip /test new_test"))
    assert 'new_test.zip' in os.listdir('/')
    unzip(CommandFromString(r"unzip new_test.zip"))
    assert 'new_test' in os.listdir('/')


def test_tar(fs: FakeFilesystem, fake_logger_info_call: Mock, fake_project_dir):
    fs.create_dir("other_test")
    fs.create_file(os.path.join("other_test", "hello world.txt"), contents="hello world")

    tar(CommandFromString(r"tar /other_test other_new_test"))
    assert 'other_new_test.tar.gz' in os.listdir('/')
    untar(CommandFromString('untar /other_new_test.tar.gz'))
    assert 'other_new_test' not in os.listdir('/')


def test_zip_unzip_invalid_file_path():
    with pytest.raises(InvalidFilePath):
        zip_dir(CommandFromString("zip abacaba abacaba"))
    with pytest.raises(InvalidFilePath):
        unzip(CommandFromString("unzip abacaba"))


def test_zip_is_file(fs: FakeFilesystem):
    fs.create_file("test.txt")
    with pytest.raises(IsFileError):
        zip_dir(CommandFromString("zip test.txt test1"))


def test_unzip_is_dir(fs: FakeFilesystem):
    fs.makedir("test")
    with pytest.raises(IsDirectoryError):
        unzip(CommandFromString("unzip test"))


def test_zip_unzip_invalid_arguments():
    with pytest.raises(InvalidCountOfArguments):
        zip_dir(CommandFromString("zip abacaba"))
    with pytest.raises(InvalidCountOfArguments):
        unzip(CommandFromString("unzip abacaba abacaba"))
