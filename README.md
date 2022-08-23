Инструкция
1. создать директорию mkdir SendingApp и перейти в нее
2. создать виртуальное окружение и активировать его python3 -m venv venv
3. установить библиотеки pip3 install -r requirements.txt
4. создать бд postgres и поменять соответствующие настройки в sending_app/sending_app/settings.py
5. добавить токен в script.sh и запустить его . script.sh
6. запустить docker с redis docker run -d -p 6379:6379 redis
7. запустить приложение python3 manage.py runserver
8. в фоновом режиме запустить celery:
9. celery -A sending_app worker -l info &
10. celery -A sending_app beat -l info &
11. celery -A sending_app flower -A sending_app --port=5555
http://127.0.0.1:8000/docs/ - документация swagger


Добавить клиента можно по ссылке http://127.0.0.1:8000/userapi/v1/clients/

Добавить рассылку можно по ссылке http://127.0.0.1:8000/mailingapi/v1/mailing/


Таска на рассылку отрабатывает каждую минуту, настроить можно в settings.py


