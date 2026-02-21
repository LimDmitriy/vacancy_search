import pytest

from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("Dev1", "Python dev", 150000, {"name": "Москва"}, "http://example.com/1", "Полная занятость"),
        Vacancy("Dev2", "Backend dev", 180000, {"name": "СПб"}, "http://example.com/2", "Удалённо"),
        Vacancy("Dev3", "Junior", 90000, {"name": "Казань"}, "http://example.com/3", "Гибкий график"),
    ]


@pytest.fixture
def vacancy_data_dict():
    return {
        "name": "Python Developer",
        "description": "<highlighttext>Опыт</highlighttext> работы от 3 лет.",
        "salary": {"from": 150000, "to": 200000},
        "area": "Москва",
        "url": "https://hh.ru/vacancy/123456",
        "work_format": "Удаленная работа",
    }


@pytest.fixture
def vacancy_dict_list():
    return [
        {
            "name": "Backend Developer",
            "snippet": {"requirement": "Знание Python и Django"},
            "salary": {"from": 120000},
            "area": {"name": "Санкт-Петербург"},
            "alternate_url": "https://hh.ru/vacancy/123",
            "employment": {"name": "Полная занятость"},
        },
        {
            "name": "Junior Python Developer",
            "snippet": {"requirement": "Желание учиться"},
            "salary": {},
            "area": {"name": "Казань"},
            "alternate_url": "https://hh.ru/vacancy/456",
            "employment": {"name": "Частичная занятость"},
        },
    ]
