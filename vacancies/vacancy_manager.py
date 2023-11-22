from .abstract_saver import AbstractSaver
import json


class JSONSaver(AbstractSaver):
    def __init__(self, file_path):
        self.file_path = file_path
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)

    def get_vacancies_by_salary(self, salary):
        filtered_vacancies = [vacancy for vacancy in self.vacancies if vacancy.salary == salary]
        return filtered_vacancies

    def delete_vacancy(self, vacancy):
        self.vacancies = [v for v in self.vacancies if v != vacancy]

    def save_to_file(self):
        data = []
        for vacancy in self.vacancies:
            data.append({
                "title": vacancy.title,
                "link": vacancy.link,
                "salary": vacancy.salary,
                "description": vacancy.description
            })

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
