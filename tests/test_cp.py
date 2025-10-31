import os
from unittest.mock import Mock

from pyfakefs.fake_filesystem import FakeFilesystem

from src.classes.command import CommandFromString
from src.commands.cp import cp


def test_cp(fs: FakeFilesystem, fake_logger_info_call: Mock, fake_project_dir):
    fs.create_dir("test")
    fs.create_file(os.path.join("test", "hello world.txt"), contents="hello world")
    fs.create_file("okak.txt", contents="Окак")

    cp(CommandFromString(r"cp test/hello\ world.txt test/'goodbye world.txt'"))
    assert 'goodbye world.txt' in os.listdir('/test')
    cp(CommandFromString('cp -r test/ other_test'))
    assert 'other_test' in os.listdir('/')

# def test_permissions_in_files(fs: FakeFilesystem, fake_logger_error_call: Mock):
#     fs.create_file("hello world.txt", contents="hello world")
#     fs.chmod("hello world.txt", 0)
#     ls(Command(f'ls -l /'))
#     out = fake_logger_error_call.call_args.args[0]
#     assert "Недостаточно прав доступа" in str(out)
#
#
# def test_ls_is_file(fs: FakeFilesystem):
#     fs.create_file("test.txt")
#     with pytest.raises(IsFileError):
#         ls(Command("ls test.txt"))
#
#
# def test_ls_invalid_path():
#     with pytest.raises(InvalidFilePath):
#         ls(Command("ls abacaba"))
