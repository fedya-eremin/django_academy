# django_academy
[![Python package](https://github.com/sunfireaegis/django_academy/actions/workflows/python-package.yml/badge.svg)](https://github.com/sunfireaegis/django_academy/actions/workflows/python-package.yml)
[![Django CI](https://github.com/sunfireaegis/django_academy/actions/workflows/django.yml/badge.svg?branch=dev)](https://github.com/sunfireaegis/django_academy/actions/workflows/django.yml)

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
из них предусмотрено значение по умолчанию. Пример представлен \
в .env.example, для использования необходимо убрать расширение \
файла
```
python3 manage.py runserver
``` 

## База данных
База данных содержит три таблицы:
- Item
- Category
- Tag

Данные для примера находятся в фикстуре в приложении catalog

Более подробно связи в таблице можно изучить в https://app.quickdatabasediagrams.com/#/d/bgWQtS
