from abc import ABC, abstractmethod
import requests

class APIClient(ABC):
    """
    Абстрактный базовый класс для взаимодействия с различными API.

    Методы:
    get_companies(company_ids): Получает данные о компаниях по их идентификаторам.
    get_vacancies(company_id): Получает данные о вакансиях компании по ее идентификатору.
    """

    @abstractmethod
    def get_companies(self, company_ids):
        pass

    @abstractmethod
    def get_vacancies(self, company_id):
        pass


class HHAPI(APIClient):
    """
    Класс HHAPI предоставляет методы для взаимодействия с публичным API сайта hh.ru.
    Позволяет получать данные о компаниях и их вакансиях.

    Атрибуты:
    BASE_URL (str): Базовый URL для API hh.ru.

    Методы:
    get_companies(company_ids): Получает данные о компаниях по их идентификаторам.
    get_vacancies(company_id): Получает данные о вакансиях компании по ее идентификатору.
    """

    BASE_URL = 'https://api.hh.ru/'

    def get_companies(self, company_ids):
        """
        Метод получает данные о компаниях по их идентификаторам.

        Аргументы метода:
        company_ids (list): Список идентификаторов компаний.

        Метод возвращает:
        list: Список данных о компаниях в формате JSON.
        """
        companies = []
        for company_id in company_ids:
            response = requests.get(f'{self.BASE_URL}employers/{company_id}')
            if response.status_code == 200:
                companies.append(response.json())
        return companies

    def get_vacancies(self, company_id):
        """
        Метод получает данные о вакансиях компании по ее идентификатору.

        Аргументы метода:
        company_id (int): Идентификатор компании.

        Метод возвращает:
        list: Список данных о вакансиях в формате JSON.
        """
        vacancies = []
        page = 0
        while True:
            response = requests.get(f'{self.BASE_URL}vacancies', params={'employer_id': company_id, 'page': page})
            if response.status_code == 200:
                data = response.json()
                vacancies.extend(data['items'])
                if data['pages'] - page <= 1:
                    break
                page += 1
            else:
                break
        return vacancies
