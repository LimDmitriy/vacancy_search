import json
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, List


class AbstractFileManager(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def get_vacancy(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(AbstractFileManager):
    """Класс для работы с JSON файлами"""

    def __init__(self, file_name: str = "./data/vacancies.json"):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.__file_name = os.path.join(base_dir, file_name)
        os.makedirs(os.path.dirname(self.__file_name), exist_ok=True)

    def get_vacancy(self) -> List[Dict[str, Any]]:
        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_vacancy(self, new_vacancy: Dict[str, Any]) -> None:
        data = self.get_vacancy()
        new_url = new_vacancy.get("url", "").strip()
        if not new_url or any(vac.get("url", "").strip() == new_url for vac in data):
            return

        data.append(new_vacancy)
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self) -> None:
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump([], file)
