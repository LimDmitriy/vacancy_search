import re
from typing import Any, Dict


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "snippet", "salary", "area", "alternate_url", "work_format")

    def __init__(self, name: str, snippet: str, salary: int, area: str, alternate_url: str, work_format: str) -> None:
        self.name = name
        self.area = area.get("name", "Не указано")
        self.work_format = work_format or "Не указано"
        self.snippet = snippet or "Не указано"
        self.salary = self._validate_salary(salary)
        self.alternate_url = alternate_url

    def __str__(self) -> str:
        city = self.area.get("name") if isinstance(self.area, dict) else self.area
        return (
            f"Название: {self.name}\n"
            f"Зарплата: {self.salary if self.salary else 'Не указано'}\n"
            f"Город: {city}\n"
            f"Формат работы: {self.work_format}\n"
            f"Описание: {self._clean_description()}\n"
            f"Ссылка: {self.alternate_url}\n"
        )

    def _clean_description(self) -> str:
        """Удаляет теги <highlighttext> и сокращает длинное описание"""
        clean = re.sub(r"</?highlighttext>", "", self.snippet)
        return clean[:300] + ("..." if len(clean) > 300 else "")

    def _validate_salary(self, salary_data: dict) -> int:
        """Метод валидации, приводит salary к числу: берёт 'from' или 'to' если есть, иначе возвращает 0"""
        if isinstance(salary_data, dict):
            return salary_data.get("from", 0) or salary_data.get("to", 0) or 0
        elif isinstance(salary_data, int):
            return salary_data
        return 0

    def __lt__(self, other) -> bool:
        """Метод сравнения зарплат двух вакансий"""
        return self.salary < other.salary

    @classmethod
    def cast_to_object_list(cls, vacancies_data: dict[str, any]) -> list["Vacancy"]:
        """Преобразует список словарей в список объектов Vacancy"""
        vacancies = []
        for vacancy in vacancies_data:
            vacancies.append(
                cls(
                    name=vacancy.get("name", "Без названия"),
                    snippet=vacancy.get("snippet", {}).get("requirement", "Нет описания"),
                    salary=vacancy.get("salary", 0),
                    area=vacancy.get("area", {}),
                    alternate_url=vacancy.get("alternate_url", ""),
                    work_format=vacancy.get("employment", {}).get("name", ""),
                )
            )
        return vacancies

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Vacancy":
        """Создаёт экземпляр Vacancy из словаря"""
        return cls(
            name=data.get("name", "Без названия"),
            snippet=data.get("description", "Нет описания"),
            salary=data.get("salary", 0),
            area={"name": data.get("area", "Не указано")},
            alternate_url=data.get("url", ""),
            work_format=data.get("work_format", "Не указано"),
        )

    def dict_vacations(self) -> Dict[str, Any]:
        """Преобразует объект в словарь для сохранения"""
        return {
            "name": self.name,
            "salary": self.salary,
            "description": self.snippet,
            "area": {"name": self.area},
            "url": self.alternate_url,
            "work_format": self.work_format,
        }
