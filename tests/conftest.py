from unittest.mock import Mock
import src.classes.json_logger
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


@pytest.fixture
def fake_project_dir(monkeypatch):
    monkeypatch.setattr(src.classes.json_logger, "UNDO_HISTORY_FILE", "/.undo_history.jsonl")
