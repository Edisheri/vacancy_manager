import requests
from .abstract_api import AbstractAPI
from vacancies.vacancy import Vacancy

class HeadHunterAPI(AbstractAPI):
    base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query):
        params = {"text": search_query, "per_page": 100, "page": 0}
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        vacancies_data = response.json()

        vacancies = []
        for item in vacancies_data.get('items', []):
            vacancy = Vacancy(
                title=item['name'],
                link=item['alternate_url'],
                salary=item.get('salary'),
                description=item['snippet']['requirement']
            )
            vacancies.append(vacancy)
        return vacancies
