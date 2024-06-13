import requests
import psycopg2
from config import DB_CONFIG


class DataLoader:
    """
        Класс DataLoader для загрузки данных о компаниях и вакансиях с сайта hh.ru в базу данных PostgreSQL.

        Методы:
        - __init__: Инициализирует соединение с базой данных и создает курсор.
        - load_data: Загружает данные о компаниях и вакансиях, вызывая соответствующие методы.
        - load_companies: Загружает данные о компаниях по их идентификаторам из API hh.ru и вставляет в таблицу companies.
        - load_vacancies: Загружает данные о вакансиях компаний по их идентификаторам из API hh.ru и вставляет в таблицу vacancies.
        - close: Закрывает курсор и соединение с базой данных.

        Исключения:
        - Выводит сообщение об ошибке в случае неудачного запроса к API hh.ru.
        """

    def __init__(self):
        """Инициализирует соединение с базой данных PostgreSQL и создает курсор."""
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()

    def load_data(self, company_ids):
        """
        Метод загружает данные о компаниях и вакансиях, вызывая соответствующие методы.
        Аргументы метода:
        company_ids (list)-> список идентификаторов компаний.
        """
        self.load_companies(company_ids)
        self.load_vacancies(company_ids)
        self.conn.commit()

    def load_companies(self, company_ids):
        """
        Метод загружает данные о компаниях по их идентификаторам из API hh.ru и вставляет в таблицу companies.
        Аргументы метода:
        company_ids (list) -> cписок идентификаторов компаний.
        """
        for company_id in company_ids:
            response = requests.get(f'https://api.hh.ru/employers/{company_id}')
            if response.status_code == 200:
                company = response.json()
                self.cursor.execute(
                    "INSERT INTO companies (id, name, url) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING",
                    (company['id'], company['name'], company['alternate_url'])
                )
            else:
                print(f"Не удалось получить вакансии для компании c id {company_id}")

    def load_vacancies(self, company_ids):
        """
        Метод загружает данные о компаниях по их идентификаторам из API hh.ru и вставляет в таблицу vacancies.
        Аргументы метода:                                                                                        
        company_ids (list) -> cписок идентификаторов компаний.                                                   
        """
        for company_id in company_ids:
            response = requests.get(f'https://api.hh.ru/vacancies?employer_id={company_id}')
            if response.status_code == 200:
                vacancies = response.json().get('items', [])
                for vacancy in vacancies:
                    salary_from = vacancy.get('salary', {}).get('from') if vacancy.get('salary') else None
                    salary_to = vacancy.get('salary', {}).get('to') if vacancy.get('salary') else None
                    self.cursor.execute(
                        """
                        INSERT INTO vacancies (company_id, title, salary_from, salary_to, url)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        (
                            company_id,
                            vacancy['name'],
                            salary_from,
                            salary_to,
                            vacancy['alternate_url']
                        )
                    )
            else:
                print(f"Не удалось получить вакансии для компании c id {company_id}")

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    from src.utils import create_tables

    create_tables()

    company_ids = [9420, 962651, 32456, 25213]
    # Пример списка отобранных мною компаний
    loader = DataLoader()
    loader.load_data(company_ids)
    loader.close()
