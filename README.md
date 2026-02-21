# Парсер вакансий с hh.ru
![Python](https://img.shields.io/badge/python-3.12-blue)
![Poetry](https://img.shields.io/badge/poetry-enabled-blueviolet)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Code style](https://img.shields.io/badge/code%20style-black-000000)
## 📌 Описание

Консольное приложение для работы с вакансиями, полученными через API hh.ru.  
Позволяет искать, фильтровать, сортировать и сохранять вакансии в JSON-файл.  
Реализовано с использованием ООП (абстрактные классы, SOLID-принципы).

---
## 🏗 Архитектура проекта

Проект построен по принципам SOLID:

- `BasicClass` — абстрактный класс для работы с API
- `HeadHunterAPI` — реализация работы с hh.ru
- `Vacancy` — класс вакансии
- `JSONSaver` — сохранение и загрузка вакансий
- `user_interaction()` — консольный интерфейс
---

## ⚙️ Возможности

- Получение вакансий по ключевому слову с hh.ru
- Сортировка по зарплате
- Фильтрация по ключевым словам и минимальной зарплате
- Сохранение и загрузка вакансий из файла
- Удобный и структурированный вывод вакансий в консоль

---

## 🚀 Установка и запуск
1. Клонируйте репозиторий:
```
git clone https://github.com/LimDmitriy/hh-vacancy-parser
```
2. Установите зависимости:
```
poetry install
```

3. Запуск проекта
```
poetry run python main.py
```

---

## 🧪 Тестирование
1. Запуск тестов
```
poetry run pytest
```
2. Проверка покрытия тестами 
```
poetry run pytest --cov
```
---
## 💻 Стек технологий

- `ООП (с абстрактными базовыми классами)`
- `Консольный интерфейс`
- `requests`
- `pytest`
- `pytest-cov`
- `re`
- `json`
- `black`
- `isort`
- `flake8`
- `mypy`

---
