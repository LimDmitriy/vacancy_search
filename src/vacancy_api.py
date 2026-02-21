from abc import ABC, abstractmethod
from typing import Any, Dict, List

import requests


class BasicClass(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def _connect_api(self, params: dict[str, Any]) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_vacancies(self, vacation: str) -> dict[str, Any]:
        pass


class HeadHunterAPI(BasicClass):
    """Класс для работы с API сервиса с вакансиями"""

    def __init__(self) -> None:
        self._url = "https://api.hh.ru/vacancies"

    def _connect_api(self, params: dict[str, Any]) -> List[Dict[str, Any]]:
        """Приватный метод для подключения к API и получения данных"""
        try:
            response = requests.get(self._url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data.get("items", [])
            else:
                print(f"Ошибка запроса: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return []

    def get_vacancies(self, vacation: str) -> list[Dict[str, Any]]:
        """Метод для получения вакансий по ключевому слову"""
        if not vacation:
            raise ValueError(("Заполните поле ввода"))
        params = {"text": vacation, "per_page": 20}
        vacancies = self._connect_api(params)
        return vacancies
