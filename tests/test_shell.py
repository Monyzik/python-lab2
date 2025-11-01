from pyfakefs.fake_filesystem import FakeFilesystem

from src.common.set_default_logging_config import set_default_logging_config
from src.system.shell import Shell


def test_shell(fs: FakeFilesystem, fake_logger_error_call, fake_project_dir):
    set_default_logging_config()
    shell = Shell("/")
    shell.complete_command("helloworld")
    out = str(fake_logger_error_call.call_args.args[0])
    assert out == "Не удалось найти команду: helloworld"
    shell.complete_command("mv history1 history_moved -r")
    out = str(fake_logger_error_call.call_args.args[0])
    assert out == "Недопустимый параметр: 'r', для команды mv"
