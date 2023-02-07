# django_academy
Проект содержит следущие ветки:
- dev для текущего состояния
- master для стабильной версии
## Установка
```
git clone https://github.com/sunfireaegis/django_academy.git
cd django_academy
```
Для запуска последней версии (тестирование):
```git switch dev```
```
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 manage.py runserver
``` 
> SECRET_KEY, DEBUG, DATABASE_NAME, DATABASE_USER,DATABASE_PASS \
и ALLOWED_HOSTS следует указать в файле .env. Для первых двух \
из них предусмотрено значение по умолчанию.
