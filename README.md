# XML/JSON Mapper

Необходимо очень часто импортировать данные из большого количества различных внешних xml/json источников в существующую реляционную модель данных.
Стоит учесть, что структура и формат данных источника и конечной модели могут существенно различаться, иметь взаимозависимости(например документ содержащий множество зависимых M2M данных вида событие-дата-место), а данные импортироваться лишь частично.

Задача: спроектировать и реализовать модуль маппера, который позволит гибко, быстро и просто собирать данные из внешних источников и складывать в существующие Django модельки.
* в рамках тестового задания достаточно реализовать RSS feed в качестве источника данных
* при проектировании следует учесть возможность подключения других произвольных источников данных в будущем
* функционал должен быть покрыт тестами
* тестовое задание должно быть реализовано в виде отдельного модуля или django app


## Installation
```
$ pip install -r requirements.txt
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py createsuperuser
```

## Run ETL for habrahabr.ru
`$ ./manage.py habr_etl`

## Run server and check results
`$ ./manage.py runserver`
Then open `localhost:8000` and you will see collected items for Author and Aticle models

## Run mapper tests
```
$ python -m unittest mapper/tests.py
```