from unittest.mock import patch

from src.vacancy_api import HeadHunterAPI


def test_get_vacancies_from_api():
    with patch.object(HeadHunterAPI, "get_vacancies", return_value=[{"name": "Test"}]) as mock_api:
        api = HeadHunterAPI()
        result = api.get_vacancies("Python")
        assert result == [{"name": "Test"}]
        mock_api.assert_called_once_with("Python")
