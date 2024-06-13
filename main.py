from src.utils import create_tables
from src.vacancy import DataLoader
from src.db_manager import DBManager
from tabulate import tabulate


if __name__ == '__main__':
    """
    Главный модуль проекта, отвечающий за создание таблиц, 
    загрузку данных и вывод информации о компаниях и вакансиях.


    Основные шаги выполнения программы:
    1. Создание таблиц в базе данных PostgreSQL с помощью функции `create_tables` 
    из модуля `utils`.
    2. Загрузка данных о компаниях и их вакансиях с сайта hh.ru 
    с использованием класса `DataLoader` из модуля `vacancy`.
    3. Получение и вывод информации о компаниях и вакансиях с помощью класса `DBManager` 
    из модуля `db_manager`.


    Функции:
    - `create_tables()`: Создает необходимые таблицы в базе данных PostgreSQL.
    - `DataLoader`: Класс для загрузки данных о компаниях и вакансиях с сайта hh.ru.
    - `DBManager`: Класс для управления данными в базе данных PostgreSQL и выполнения запросов на получение данных.


    Пример использования:
    1. Создать таблицы в базе данных.
    2. Загрузить данные о компаниях и их вакансиях.
    3. Получить и вывести в консоль информацию о компаниях и вакансиях в табличном формате.


    """
    # Создание таблиц
    create_tables()


    # Загрузка данных
    company_ids = [9420, 962651, 32456, 25213]
    loader = DataLoader()
    loader.load_data(company_ids)


    db_manager = DBManager()


    # Печать данных в табличном формате
    companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
    print("Companies and Vacancies Count:")
    print(tabulate(companies_and_vacancies_count, headers=["Company", "Vacancies Count"]))


    all_vacancies = db_manager.get_all_vacancies()
    print("\nAll Vacancies:")
    print(tabulate(all_vacancies, headers=["Company", "Title", "Salary From", "Salary To", "URL"]))


    avg_salary = db_manager.get_avg_salary()
    print(f"\nAverage Salary: {avg_salary}")


    vacancies_with_higher_salary = db_manager.get_vacancies_with_higher_salary()
    print("\nVacancies with Higher Salary than Average:")
    print(tabulate(vacancies_with_higher_salary, headers=["Company", "Title", "Salary From", "Salary To", "URL"]))


    keyword = "логист"
    vacancies_with_keyword = db_manager.get_vacancies_with_keyword(keyword)
    print(f"\nVacancies with Keyword '{keyword}':")
    print(tabulate(vacancies_with_keyword, headers=["Company", "Title", "Salary From", "Salary To", "URL"]))


    db_manager.close()
