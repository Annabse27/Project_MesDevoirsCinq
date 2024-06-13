Этот проект собирает данные о компаниях и их вакансиях с сайта hh.ru и загружает их в базу данных PostgreSQL. Затем вы можете использовать класс `DBManager` для работы с этими данными.

Актуальная структура проекта 

```
Project_MesDevoirsCinq/
├── src/
│   ├── __init__.py
│   ├── hh.py
│   ├── utils.py
│   ├── vacancy.py
│   ├── db_manager.py
├── config.py
├── main.py
├── .gitignore
├── Readme.md
└── pyproject.toml
```

**src/hh.py**: Получение данных с сайта hh.ru. 
Используем библиотеку `requests` для взаимодействия с API hh.ru.

**src/utils.py**: Проектирование таблиц в БД PostgreSQL.
Создаем таблицы для хранения данных о работодателях и вакансиях.

**src/vacancy.py**: Заполнение таблиц данными.

**src/db_manager.py**: Класс DBManager для работы с данными в БД.

