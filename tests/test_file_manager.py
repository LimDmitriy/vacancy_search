from unittest.mock import patch

from src.file_manager import JSONSaver


def test_add_and_get_vacancy():
    with patch("builtins.open", create=True), patch("json.dump"), patch("json.load", return_value=[]):
        saver = JSONSaver("test.json")
        vacancy_data = {
            "name": "Test",
            "salary": 100000,
            "description": "desc",
            "area": {"name": "Москва"},
            "url": "http://url",
            "work_format": "удалённо",
        }
        with patch("os.path.exists", return_value=True):
            saver.add_vacancy(vacancy_data)
            data = saver.get_vacancy()
            assert isinstance(data, list)
