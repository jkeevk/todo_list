### Задача:

**[Тестовое задание](test_case.md)**

### Порядок запуска:

1. Создайте и активируйте виртуальное окружение:

```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate  # Для Windows
```

2. После активации виртуального окружения установите необходимые зависимости:

`pip install -r requirements.txt`

3. Создайте БД в PostgreSQL
   Переменные окружения не использовались, поэтому нужно изменить настройки подключения DATABASES в `todolist/settings.py`

`createdb -h localhost -p 5432 -U postgres god_todo_list`

4. Создание миграций приложения для базы данных:

`python manage.py migrate`

5. После того как PostgreSQL будет готов, запустите сервер:

`python manage.py runserver`

Выполнять запросы можно через **[requests.http](requests.http)**

Вы можете использовать HTTP-запросы с помощью расширения для вашего редактора кода (например, VSCode) или через инструмент requests для тестирования серверных API.
