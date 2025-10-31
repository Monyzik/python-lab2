from unittest.mock import Mock

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from src.classes.command import CommandFromString
from src.classes.exeptions import InvalidFilePath, IsDirectoryError, InvalidCountOfArguments
from src.commands.cat import cat


def test_cat(fs: FakeFilesystem, fake_logger_info_call: Mock):
    fs.create_file("test.txt", contents="hello world")
    cat(CommandFromString("cat test.txt"))
    out = fake_logger_info_call.call_args.args[0]
    assert "hello world" in out


def test_cat_jpg(fs: FakeFilesystem, fake_logger_info_call: Mock):
    fs.create_file("okak.jpg",
                   contents=b"\x92\xe7o\xfa\xbb\x7fw\xbf \xbc\x070&;\xca}\xb7B\xd9\xfa\xd5\xd4_#\x97F\'\xedqH\xfe\xd9\x82\xb1\xaeI\xf4\rr\xf4\x83H\xe5\xe3$\x19\xe2y\xbbG\x9b\x7f\xf7b\xefD\x18\x1f\x12\xc7\xcc\xb7\xff\x00g\xff\xd9")
    cat(CommandFromString("cat okak.jpg"))
    out = fake_logger_info_call.call_args.args[0]
    assert "67" in str(out)


def test_cat_is_dir(fs: FakeFilesystem):
    fs.create_dir("test_dir")
    with pytest.raises(IsDirectoryError):
        cat(CommandFromString("cat test_dir/"))


def test_cat_invalid_path():
    with pytest.raises(InvalidFilePath):
        cat(CommandFromString("cat abacaba"))


def test_cat_invalid_argument_count():
    with pytest.raises(InvalidCountOfArguments):
        cat(CommandFromString("cat file1.txt file2.txtxzl"))
