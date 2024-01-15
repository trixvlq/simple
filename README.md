# Тестовое задание

Стек:

<img src="https://img.shields.io/badge/Python-4169E1?style=for-the-badge"/> <img src="https://img.shields.io/badge/Django-008000?style=for-the-badge"/> <img src="https://img.shields.io/badge/DRF-800000?style=for-the-badge"/> <img src="https://img.shields.io/badge/Docker-00BFFF?style=for-the-badge"/> <img src="https://img.shields.io/badge/PostgreSQL-87CEEB?style=for-the-badge"/> <img src = "https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"> <img src = "https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white">
# Описание проекта:
Этот проект представляет собой выполнение тестового задания от компании SimpleSolutions. Он представляет собой простой сайт, в котором оплата проводится с использованием Stripe, а данные о продуктах записываются в PostgreSQL.

Сайт обладает следующим функционалом:

- Покупка товара
- Создание товара
- Создание промокодов
- Подключение налогов
- Авторизация пользователя
- Конвертация валют
- Оплата с помощью Stripe

# Как запустить проект

1. Клонировать репозиторий:

```
https://github.com/trixvlq/simple.git
```
2. Перейти в директорию проекта:
```
cd simple
```
3. В директории `simple` нужно создать файл `.env` и задать в нём следующие значения:
```
api_key=ваш ключ от stripe
SECRET_KEY=django sercet key
DEBUG=True
DB_HOST=simple_database
DB_NAME=simple
DB_USER=postgres
DB_PASSWORD=password
DB_PORT=5432
POSTGRES_DB=simple
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
```
4. Создать Docker контейнер:
```
docker-compose build
```
5. Создать миграции:
```
docker-compose run --rm simple_app sh -c "python manage.py migrate"
```
6. Запустить контейнер:
```
docker-compose up
```
Теперь проект доступен по адресу:
```
http://127.0.0.1/
```
