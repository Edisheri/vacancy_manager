from api.hh_api import HeadHunterAPI
from api.superjob_api import SuperJobAPI
from vacancies.vacancy import Vacancy
from vacancies.vacancy_manager import JSONSaver

def user_interaction():
    # Создаем экземпляры классов для работы с API
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    # Получаем вакансии с разных платформ
    hh_vacancies = hh_api.get_vacancies("Python")
    superjob_vacancies = superjob_api.get_vacancies("Python")

    # Создаем экземпляр класса для работы с вакансиями
    vacancy_manager = JSONSaver("vacancies.json")

    # Добавление вакансий
    for vacancy in hh_vacancies:
        vacancy_manager.add_vacancy(vacancy)

    for vacancy in superjob_vacancies:
        vacancy_manager.add_vacancy(vacancy)

    # Удаление вакансии
    vacancy_manager.delete_vacancy(hh_vacancies[0])

    # Сохранение информации о вакансиях в файл
    vacancy_manager.save_to_file()

    # Получение вакансий по определенным критериям
    filtered_vacancies = vacancy_manager.get_vacancies_by_salary("100 000-150 000 руб.")

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    # Сортировка вакансий
    sorted_vacancies = sorted(filtered_vacancies)

    # Вывод вакансий в отсортированном порядке
    for vacancy in sorted_vacancies:
        print(vacancy)

if __name__ == "__main__":
    user_interaction()
