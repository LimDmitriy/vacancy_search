class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "snippet", "salary", "area", "alternate_url", "work_format")

    def __init__(self, name, snippet, salary, area, alternate_url, work_format):
        self.name = name
        self.area = area.get("name", "Не указанно")
        self.work_format = work_format or "Не указанно"
        self.snippet = snippet or "Не указанно"
        self.salary = self._validate_salary(salary)
        self.alternate_url = alternate_url

    def _validate_salary(self, salary_data: dict) -> int:
        """Метод валидации, приводит salary к числу: берёт 'from' или 'to' если есть, иначе возвращает 0"""
        if isinstance(salary_data, dict):
            return salary_data.get("from", 0) or salary_data.get("to", 0) or 0
        return 0

    def __lt__(self, other):
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

    def dict_vacations(self):
        return {
            "name": self.name,
            "salary": self.salary,
            "description": self.snippet,
            "area": self.area,
            "url": self.alternate_url,
            "work_format": self.work_format,
        }
