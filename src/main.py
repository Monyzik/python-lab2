import sys

from src.system.shell import Shell
from src.common.set_default_logging_config import set_default_logging_config


def main() -> None:
    """
    Запускает основную часть программы
    :return: Данная функция ничего не возвращает
    """
    set_default_logging_config()
    shell = Shell(current_dir="~")
    while sys.stdin:
        try:
            command = input(f"[{shell.get_cur_dir()}] ")
            if command == 'exit':
                break
            shell.complete_command(command)
        except (EOFError, KeyboardInterrupt):
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()
