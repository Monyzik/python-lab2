import os


def tokenization_command(command: str) -> list[str]:
    """
    Декомпозирует строку на отдельные блоки с учетом специальных символов, таких как: ', ", /.
    :param command: Строка команды.
    :return: Возвращает list[str] содержащий отдельные компоненты команды.
    """
    length = len(command)
    result = []
    i = 0
    current = ""
    while i < length:
        if i + 1 < length and command[i] == '\\':
            current += command[i + 1]
            i += 1
        elif command[i] == '\'':
            i += 1
            while i < length and command[i] != '\'':
                current += command[i]
                i += 1
        elif command[i] == '\"':
            i += 1
            while i < length and command[i] != '\"':
                current += command[i]
                i += 1
        elif command[i] == ' ' or command[i] == '\t':
            if current:
                result.append(current)
            current = ""
        else:
            current += command[i]
        i += 1
    if current:
        result.append(current)
    return result


class Command:
    def __init__(self, main_command: str, args: list[str], params: list[str]) -> None:
        """
        Инициализирует команду
        :param main_command: основная команда, которая будет выполнена
        :param args: аргументы команды
        :param params: параметры/флаги вызова команды
        """
        self.main_command = main_command
        self.args = args
        self.params = params


class CommandFromString(Command):
    def __init__(self, command_str: str) -> None:
        """
        Инициализирует команду из строки
        :param command_str: команда в строковом формате
        """
        self.command_str = command_str
        self.command = tokenization_command(command_str)
        super().__init__(*self.parse_command())

    def parse_command(self) -> tuple[str, list[str], list[str]]:
        """
        Парсит команду на значения: основная команда, аргументы и параметры.
        :return: Ничего не возвращает.
        """
        args, params = [], []
        if not self.command:
            raise ValueError("Пустая команда")
        main_command = self.command[0]
        for i in range(1, len(self.command)):
            item = self.command[i]
            if item[0] == '-':
                for j in range(1, len(item)):
                    params.append(item[j])
            else:
                args.append(os.path.expanduser(item))
        return main_command, args, params

    def __str__(self):
        return self.command_str
