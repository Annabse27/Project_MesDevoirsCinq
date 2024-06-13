import psycopg2
from config import DB_CONFIG


def create_tables():
    """
    Проектирование таблиц в БД PostgreSQL.
    Создаем таблицы, если они еще не существуют
    1. companies
    2. vacancies
    для хранения данных о работодателях и вакансиях.
    -----------
    Примеч: FOREIGN KEY (company_id) REFERENCES companies (id) ON DELETE CASCADE
    - ограничение внешнего ключа, удаляющее все связанные вакансии
    при удалении компании.
    -----------
    Функция подключается к базе данных PostgreSQL,
    выполняет команды создания таблиц
    и закрывает соединение.

    Исключения: psycopg2.DatabaseError: Обработка ошибок, связанных с базой данных.
    """
    commands = (
        """
        CREATE TABLE IF NOT EXISTS companies (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            url VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS vacancies (
            id SERIAL PRIMARY KEY,
            company_id INTEGER NOT NULL,
            title VARCHAR(255) NOT NULL,
            salary_from INTEGER,
            salary_to INTEGER,
            url VARCHAR(255) NOT NULL,
            FOREIGN KEY (company_id) REFERENCES companies (id) ON DELETE CASCADE
        )
        """
    )

    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
