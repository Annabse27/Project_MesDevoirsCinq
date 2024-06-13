import psycopg2
from config import DB_CONFIG


def reset_db():
    """
    Скрипт, чтобы сбросить базу данных и создать таблицы заново
    """
    commands = (
        "DROP TABLE IF EXISTS vacancies",
        "DROP TABLE IF EXISTS companies"
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


if __name__ == '__main__':
    reset_db()
