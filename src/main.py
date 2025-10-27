import os
import sys

from src.set_default_logging_config import set_default_logging_config
from src.shell import Shell


def main() -> None:
    """
    Обязательная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    set_default_logging_config()
    shell = Shell(cur_dir="~")
    while sys.stdin:
        try:
            command = input(f"[{os.getcwd()}] ")
            if command == 'exit':
                break
            shell.complete_command(command)
        except (EOFError, KeyboardInterrupt):
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()
