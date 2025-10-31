import pytest

from src.classes.command import CommandFromString


def test_command_tokenizer():
    command = CommandFromString("ls -t   abacaba\t   aba\\ aba\" \"aba' 'aba  -l")
    assert command.main_command == "ls"
    assert command.args == ["abacaba", "aba aba aba aba"]
    assert command.params == ['t', 'l']

    command = CommandFromString("cat 'hello my name Fedia.txt'")
    assert command.main_command == "cat"
    assert command.args == ["hello my name Fedia.txt"]

    command = CommandFromString("cp \"hello my name Fedia.pdf\"")
    assert command.main_command == "cp"
    assert command.args == ["hello my name Fedia.pdf"]


def test_empty_command_tokenizer():
    with pytest.raises(ValueError):
        CommandFromString("")
