DATAFORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FILE = "../shell.log"
HISTORY_FILE = "../.history"
COMMAND_INPUT_LOGGER_NAME, COMMAND_OUTPUT_LOGGER_NAME = "command_input_logger", "command_output_logger"
ERROR_LOGGER_NAME = "error_logger"
FILE_LOGGER_NAME = "file_logger"

from src.commands.cat import cat
from src.commands.ls import ls
from src.commands.cd import cd
from src.commands.cp import cp
from src.commands.mv import mv
from src.commands.rm import rm

COMMANDS = {"cat": cat, "ls": ls, "cd": cd, "cp": cp, "mv": mv, "rm": rm}
