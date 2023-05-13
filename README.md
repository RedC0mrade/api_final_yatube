# api_final
### Описание
Благодаря этому проекту можно будет работать чезер программный интерфейс приложения
### Технологии
Django==3.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==9.3.0
PyJWT==2.1.0
requests==2.26.0
django-filter==23.2
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
- Выполнить миграции:
```
python manage.py migrate
```
- Запустить проект:
```
python manage.py runserver
```
