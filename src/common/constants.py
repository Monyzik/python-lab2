from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent.parent
DATAFORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FILE = f"{PROJECT_DIR}/shell.log"
HISTORY_FILE = f"{PROJECT_DIR}/.history"
UNDO_HISTORY_FILE = f"{PROJECT_DIR}/.undo_history.jsonl"
TRASH_DIR = f"{PROJECT_DIR}/.trash"
COMMAND_INPUT_LOGGER_NAME, COMMAND_OUTPUT_LOGGER_NAME = "command_input_logger", "command_output_logger"
ERROR_LOGGER_NAME = "error_logger"
FILE_LOGGER_NAME = "file_logger"
