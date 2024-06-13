import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'hh_db'),
    'user': os.getenv('DB_USER', 'annazav'),
    'password': os.getenv('DB_PASSWORD', '12345')
}

"""
    Конфигурация подключения к базе данных PostgreSQL.
    
    Переменная `DB_CONFIG` представляет собой словарь с параметрами подключения к 
    базе данных PostgreSQL, полученными из переменных окружения:
    - `host`: адрес сервера базы данных (по умолчанию, 'localhost').
    - `database`: имя базы данных (по умолчанию, 'hh_db').
    - `user`: имя пользователя для подключения к базе данных (по умолчанию, 'annazav').
    - `password`: пароль пользователя для подключения к базе данных (по умолчанию, '12345').
    
    Эти параметры используются библиотекой `psycopg2` для установления соединения с 
    базой данных.
    
    1. **Подключение к PostgreSQL:** (bash)
       sudo -u postgres psql
    
    2. **Создать пользователя:** (sql)
       CREATE USER annazav WITH PASSWORD '12345';
    
    3. **Создать базу данных и назначить владельца:** (sql)
       CREATE DATABASE hh_db OWNER annazav;
    
    4. **Дать пользователю все привилегии на эту базу данных:** (sql)
       GRANT ALL PRIVILEGES ON DATABASE hh_db TO annazav;
    
    5. **Выход из psql:** (sql)
       \\q
    
    6. **Проверка подключения к базе данных:** (python)
       import psycopg2
       try:
           conn = psycopg2.connect(**DB_CONFIG)
           print("Подключение успешно")
           conn.close()
       except Exception as e:
           print(f"Ошибка подключения: {e}")

"""

