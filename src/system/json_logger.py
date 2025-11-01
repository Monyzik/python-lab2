import json
import os.path
from datetime import datetime

from src.common.constants import UNDO_HISTORY_FILE


class JsonLogger:
    def __init__(self, function: str | None = "", from_path: str = "", to_path: str = "", params: list[str] | None = None) -> None:
        """
        Инициализирует json значения команды
        :param function: основная операция
        :param from_path: Директория из которой произведена операция.
        :param to_path: Директория в которую произведена операция.
        :param params: Параметры, которые были переданы при выполнении команды.
        """
        self.function = function
        self.from_path = os.path.expanduser(from_path)
        self.to_path = os.path.expanduser(to_path)
        self.params = params

    def format(self) -> str:
        """
        Составляет json.
        :return: Возвращает json строку.
        """
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'function': self.function,
            'to_path': os.path.abspath(os.path.expanduser(self.to_path)),
            'from_path': os.path.abspath(os.path.expanduser(self.from_path)),
            'params': self.params,
        }

        return json.dumps(log_entry, ensure_ascii=False)

    def write(self) -> None:
        """
        Записывает json в файл.
        :return: Ничего не возвращает.
        """
        with open(UNDO_HISTORY_FILE, 'a') as file:
            file.write(self.format() + '\n')
