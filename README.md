# django_academy
[![Python package](https://github.com/sunfireaegis/django_academy/actions/workflows/python-package.yml/badge.svg)](https://github.com/sunfireaegis/django_academy/actions/workflows/python-package.yml)

![GitHub last commit](https://img.shields.io/github/last-commit/sunfireaegis/django_academy)
![GitHub issues](https://img.shields.io/github/issues/sunfireaegis/django_academy)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/sunfireaegis/django_academy)
Предназначен для интенсива Академии Яндекс.\
Проект содержит следущие ветки:
- dev для текущего состояния
- master для стабильной версии
## Установка
```
git clone https://github.com/sunfireaegis/django_academy.git
cd django_academy
```
Для запуска последней версии (вероятно, нестабильно):
```git switch dev```
```
python -m venv venv
source ./venv/bin/activate
pip install -e .
```

для установки окружения с линтерами - ```pip install -e .[dev]``` \
и ```pip install -e .[test]``` с фреймворком для тестирования соответственно

## Запуск
> SECRET_KEY, DEBUG, DATABASE_NAME, DATABASE_USER,DATABASE_PASS \
и ALLOWED_HOSTS следует указать в файле .env. Для первых двух \
из них предусмотрено значение по умолчанию.
```
python3 manage.py runserver
``` 

