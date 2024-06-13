# Project_MesDevoirsCinq

Этот проект собирает данные о компаниях и их вакансиях с сайта hh.ru и загружает их в базу данных PostgreSQL. Затем вы можете использовать класс `DBManager` для работы с этими данными.

## Актуальная структура проекта

```
Project_MesDevoirsCinq/
├── src/
│   ├── __init__.py
│   ├── hh.py
│   ├── utils.py
│   ├── vacancy.py
│   ├── db_manager.py
├── config.py
├── reset_db.py
├── main.py
├── .gitignore
├── Readme.md
└── pyproject.toml
```

## Установка

### Требования

- Операционная система: Linux
- Python 3.8+
- PostgreSQL
- poetry

### Настройка окружения

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-repo/Project_MesDevoirsCinq.git
cd Project_MesDevoirsCinq
```

2. Установите зависимости с помощью poetry:

```bash
poetry install
```

3. Создайте файл `.env` в корневом каталоге проекта и добавьте следующие строки с настройками вашей базы данных:

```
DB_HOST=localhost
DB_NAME=hh_db
DB_USER=your_username
DB_PASSWORD='your_password'
```

### Настройка базы данных

1. Подключитесь к PostgreSQL:

```bash
sudo -u postgres psql
```

2. Создайте пользователя и базу данных:

```sql
CREATE USER your_username WITH PASSWORD 'your_password';
CREATE DATABASE hh_db OWNER your_username;
GRANT ALL PRIVILEGES ON DATABASE hh_db TO your_username;
\q
```

## Использование

### Сброс базы данных

Для сброса базы данных и создания таблиц заново используйте скрипт `reset_db.py`:

```bash
poetry run python reset_db.py
```

### Запуск проекта

Запустите основной модуль проекта:

```bash
poetry run python main.py
```

Этот скрипт выполнит следующие действия:
1. Создаст таблицы в базе данных PostgreSQL.
2. Загрузит данные о компаниях и их вакансиях с сайта hh.ru.
3. Выведет информацию о компаниях и вакансиях в консоль в табличном формате.

## Структура проекта

- **src/hh.py**: Получение данных с сайта hh.ru. Использует библиотеку `requests` для взаимодействия с API hh.ru.
- **src/utils.py**: Проектирование таблиц в БД PostgreSQL. Создает таблицы для хранения данных о работодателях и вакансиях.
- **src/vacancy.py**: Заполнение таблиц данными.
- **src/db_manager.py**: Класс `DBManager` для работы с данными в БД.
- **reset_db.py**: Сбрасывает базу данных и создает таблицы заново.
- **config.py**: Конфигурация подключения к базе данных PostgreSQL.
- **main.py**: Главный модуль проекта, отвечающий за создание таблиц, загрузку данных и вывод информации о компаниях и вакансиях.


Не забудьте заменить `your_username` и `your_password` на соответствующие значения для вашей системы.
