import psycopg2
from config import DB_CONFIG


class DBManager:
    """
        Класс для взаимодействия с базой данных PostgreSQL
        и выполнения различных манипуляций с данными о компаниях и вакансиях.

        Атрибуты

        conn : Подключение к базе данных PostgreSQL
        cur : Курсор для выполнения операций с базой данных

        Методы:
        -------
        get_companies_and_vacancies_count():
            Возвращает список всех компаний и количество вакансий у каждой компании.

        get_all_vacancies():
            Возвращает список всех вакансий с указанием названия компании,
            названия вакансии, зарплаты и ссылки на вакансию.

        get_avg_salary():
            Возвращает среднюю зарплату по всем вакансиям.

        get_vacancies_with_higher_salary():
            Возвращает список всех вакансий,
            у которых зарплата выше средней по всем вакансиям.

        get_vacancies_with_keyword(keyword):
            Возвращает список всех вакансий,
            в названии которых содержится переданное в метод слово.
        ----------
        close(): Закрывает подключение к базе данных и курсор.
        """

    def __init__(self):
        """
        Инициализирует соединение с базой данных PostgreSQL
        и создает курсор для выполнения операций.
        """
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """
        Возвращает список всех компаний и количество вакансий у каждой компании.
        -------
        list of tuple -> Список кортежей, где каждый кортеж содержит
        название компании и количество вакансий у этой компании.
        """
        self.cur.execute("""
            SELECT c.name, COUNT(v.id)
            FROM companies c
            JOIN vacancies v ON c.id = v.company_id
            GROUP BY c.name
        """)
        return self.cur.fetchall()

    def get_all_vacancies(self):
        """
        Возвращает список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию.
        -------
        list of tuple -> Список кортежей, где каждый кортеж содержит
        название компании, название вакансии, зарплату и ссылку на вакансию.
        """
        self.cur.execute("""
            SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
            FROM companies c
            JOIN vacancies v ON c.id = v.company_id
        """)
        return self.cur.fetchall()

    def get_avg_salary(self):
        """
        Возвращает среднюю зарплату по всем вакансиям.
        -------
        float -> Средняя зарплата по всем вакансиям.
        """
        self.cur.execute("""
            SELECT AVG((salary_from + salary_to) / 2)
            FROM vacancies
            WHERE salary_from IS NOT NULL AND salary_to IS NOT NULL
        """)
        return self.cur.fetchone()[0]

    def get_vacancies_with_higher_salary(self):
        """
        Возвращает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        -------
        list of tuple -> Список кортежей, где каждый кортеж содержит
        название компании, название вакансии, зарплату и ссылку на вакансию.
        """
        avg_salary = self.get_avg_salary()
        self.cur.execute("""
            SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
            FROM companies c
            JOIN vacancies v ON c.id = v.company_id
            WHERE (v.salary_from + v.salary_to) / 2 > %s
        """, (avg_salary,))
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """
        Возвращает список всех вакансий, в названии которых содержится
        переданное в метод слово.
        Параметр:
        keyword: str -> Ключевое слово для поиска в названиях вакансий
        -------
        list of tuple -> Список кортежей, где каждый кортеж содержит
        название компании, название вакансии, зарплату и ссылку на вакансию.
        """

        self.cur.execute("""
            SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
            FROM companies c
            JOIN vacancies v ON c.id = v.company_id
            WHERE v.title ILIKE %s
        """, (f'%{keyword}%',))
        return self.cur.fetchall()

    def close(self):
        """
        Закрывает подключение к базе данных и курсор
        """
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":

    db_manager = DBManager()
    db_manager.close()


