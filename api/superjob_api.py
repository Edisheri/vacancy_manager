import requests
from .abstract_api import AbstractAPI
from vacancies.vacancy import Vacancy

class SuperJobAPI(AbstractAPI):
    base_url = "https://api.superjob.ru/2.0/vacancies/"

    def get_vacancies(self, search_query):
        headers = {"X-Api-App-Id": 'v3.r.126843824.3a48df6e51d9485f2a5c4f1ef4f3e8ccb66845f6.42ffc2a9e9faefcddbfc7e1e2b30da00a549dcb9'}
        params = {"keyword": search_query, "count": 100}
        response = requests.get(self.base_url, headers=headers, params=params)
        response.raise_for_status()
        vacancies_data = response.json()

        vacancies = []
        for item in vacancies_data.get('objects', []):
            salary = None
            if item['payment_from'] or item['payment_to']:
                salary = f'{item["payment_from"]} - {item["payment_to"]}'
            vacancy = Vacancy(
                title=item['profession'],
                link='https://superjob.ru/' + item['link'],
                salary=salary,
                description=item['candidat']
            )
            vacancies.append(vacancy)
        return vacancies
