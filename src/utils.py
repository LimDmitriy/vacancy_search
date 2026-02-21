from src.file_manager import JSONSaver
from src.vacancy import Vacancy
from src.vacancy_api import HeadHunterAPI


def user_interaction():
    api = HeadHunterAPI()
    file = JSONSaver("./data/vacancies.json")

    while True:
        print("1. Поиск вакансий и сохранение")
        print("2. Показать топ N вакансий по зарплате")
        print("3. Поиск по ключевым словам")
        print("4. Очистить сохранённые вакансии")
        print("5. Выход")

        user_input = input("Выберите пункт меню:\n")

        if user_input == "1":
            query = input("Введите поисковый запрос: ")
            raw_vacancies = api.get_vacancies(query)
            vacancies = Vacancy.cast_to_object_list(raw_vacancies)
            for v in vacancies:
                file.add_vacancy(v.dict_vacations())
            print(f"Добавлено {len(vacancies)} вакансий.")

        elif user_input == "2":
            try:
                n = int(input("Введите количество вакансий для отображения: "))
            except ValueError:
                print("Введите число.")
                continue
            raw_data = file.get_vacancy()
            vacancies = [Vacancy.from_dict(v) for v in raw_data]
            filtered = [v for v in vacancies if v.salary > 0]
            top_vacancies = sorted(filtered, reverse=True)[:n]
            if not top_vacancies:
                print("Нет вакансий с указанной зарплатой.")
            else:
                for v in top_vacancies:
                    print(v)

        elif user_input == "3":
            keyword = input("Введите ключевое слово: ").lower()
            data = file.get_vacancy()
            matches = [Vacancy.from_dict(v) for v in data if keyword in v["description"].lower()]
            for v in matches:
                print(v)

        elif user_input == "4":
            file.delete_vacancy()
            print("Вакансии удалены.")

        elif user_input == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")
