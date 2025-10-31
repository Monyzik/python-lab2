from unittest.mock import Mock
import src.classes.json_logger
import src.commands.history
import src.common.constants
import src.common.set_default_logging_config
import src.commands.history
import src.commands.rm
import src.commands.undo
import pytest
from pytest_mock import MockerFixture


@pytest.fixture
def fake_logger_info_call(mocker: MockerFixture) -> Mock:
    mock_logger_info_call = mocker.patch("logging.Logger.info")
    return mock_logger_info_call


@pytest.fixture
def fake_logger_error_call(mocker: MockerFixture) -> Mock:
    mock_logger_info_call = mocker.patch("logging.Logger.error")
    return mock_logger_info_call


@pytest.fixture()
def fake_project_dir(monkeypatch):
    monkeypatch.setattr(src.common.constants, "PROJECT_DIR", "/")
    monkeypatch.setattr(src.common.constants, "HISTORY_FILE", "/.history")
    monkeypatch.setattr(src.common.constants, "LOG_FILE", "/shell.log")
    monkeypatch.setattr(src.common.set_default_logging_config, "LOG_FILE", "/shell.log")
    monkeypatch.setattr(src.common.set_default_logging_config, "HISTORY_FILE", "/.history")
    monkeypatch.setattr(src.commands.history, "HISTORY_FILE", "/.history")
    monkeypatch.setattr(src.commands.rm, "TRASH_DIR", "/.trash")
    monkeypatch.setattr(src.commands.undo, "UNDO_HISTORY_FILE", "/.undo_history.jsonl")
    monkeypatch.setattr(src.classes.json_logger, "UNDO_HISTORY_FILE", "/.undo_history.jsonl")
