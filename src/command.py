import os


def tokenization_command(command: str) -> list[str]:
    """
    Декомпозирует строку на отдельные блоки с учетом специальных символов, таких как: ', ", /
    :param command: Строка команды
    :return: Возвращает list[str] содержащий отдельные компоненты команды
    """
    length = len(command)
    result = []
    i = 0
    current = ""
    while i < length:
        if i + 1 < length and command[i:i + 2] == r'\ ':
            current += ' '
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
    def __init__(self, command_str: str) -> None:
        """

        :param command_id:
        :param command_str:
        """
        self.command_str = command_str
        self.command = tokenization_command(command_str)
        self.main_command = ""
        self.args = list()
        self.params = list()
        self.parse_command()

    def parse_command(self) -> None:
        if not self.command:
            raise ValueError("Пустая команда")
        self.main_command = self.command[0]
        for i in range(1, len(self.command)):
            item = self.command[i]
            if item[0] == '-':
                for j in range(1, len(item)):
                    self.params.append(item[j])
            else:
                self.args.append(os.path.expanduser(item))

    def __str__(self):
        return self.command_str

    def __repr__(self):
        return f"id={self.id}, command='{self.main_command}': args={self.args}, params={self.params}"
