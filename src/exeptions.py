class InvalidCommandName(Exception):
    def __init__(self, command: str):
        super().__init__(f"Не удалось найти команду: {command}")


class InvalidCountOfArguments(Exception):
    def __init__(self, command: str):
        super().__init__(f"Неправильное количество аргументов для команды {command}")


class InvalidAccessForFile(Exception):
    def __init__(self, path: str):
        super().__init__(f"Недостаточно прав доступа для файла {path}")


class InvalidFilePath(Exception):
    def __init__(self, path: str):
        super().__init__(f"Файл {path} не существует")


class IsDirectoryError(Exception):
    def __init__(self, command: str, path: str):
        super().__init__(f"Невозможно применить команду {command} к директории {path}")


class IsFileError(Exception):
    def __init__(self, command: str, path: str):
        super().__init__(f"Невозможно применить команду {command} к файлу {path}")


class ImpossibleToDelete(Exception):
    def __init__(self, path: str):
        super().__init__(f"Невозможно удалить {path}")
