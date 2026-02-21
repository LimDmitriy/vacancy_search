from src.vacancy import Vacancy


def test_from_dict(vacancy_data_dict):
    vacancy = Vacancy.from_dict(vacancy_data_dict)
    assert vacancy.name == "Python Developer"
    assert vacancy.salary == 150000
    assert vacancy.area == "Москва"
    assert "Опыт работы" in vacancy._clean_description()
    assert "highlighttext" not in vacancy._clean_description()


def test_dict_vacations(vacancy_data_dict):
    vacancy = Vacancy.from_dict(vacancy_data_dict)
    v_dict = vacancy.dict_vacations()
    assert v_dict["name"] == "Python Developer"
    assert v_dict["area"]["name"] == "Москва"
    assert "description" in v_dict


def test_cast_to_object_list(vacancy_dict_list):
    vacancies = Vacancy.cast_to_object_list(vacancy_dict_list)
    assert len(vacancies) == 2
    assert vacancies[0].name == "Backend Developer"
    assert vacancies[1].area == "Казань"
    assert isinstance(vacancies[0].salary, int)


def test_salary_validation():
    vacancy = Vacancy(
        name="Test",
        snippet="Описание",
        salary={"to": 90000},
        area={"name": "Екатеринбург"},
        alternate_url="http://example.com",
        work_format="Полная занятость",
    )
    assert vacancy.salary == 90000
