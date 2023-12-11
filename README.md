# Тестовое задание

Стек:

<img src="https://img.shields.io/badge/Python-4169E1?style=for-the-badge"/> <img src="https://img.shields.io/badge/Django-008000?style=for-the-badge"/> <img src="https://img.shields.io/badge/DRF-800000?style=for-the-badge"/> <img src="https://img.shields.io/badge/Docker-00BFFF?style=for-the-badge"/> <img src="https://img.shields.io/badge/PostgreSQL-87CEEB?style=for-the-badge"/> <img src = "https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"> <img src = "https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white">
# Описание проекта:
Этот проект является выпонлениием тестового задания компании SimpleSolutions, оно представляет из себя простой сайт, в котором оплата проводится с помощью Stripe, Данные о продуктах записываются в Postgresql.

Этот сайт имеет следующий функционал:

- Покупка товара
- Создание товара
- Создание промокодов
- Подключение налогов
- Авторизация пользователя
- Конвертация валют
- Оплата с помощью Stripe

# Как запустить проект

Клонировать репрозиторий

```
https://github.com/trixvlq/simple.git
```
Далее переходим в директорию
```
cd simple
```
В директории simple нужно создать .env файл и задать в нём следующие значения
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
Далее необходимо создать Docker контейнер
```
docker-compose build
```
Создать миграции
```
docker-compose run --rm simple_app sh -c "python manage.py migrate"
```
И запустить контейнер
```
docker-compose up
```
Теперь проект доступен по адресу:
```
http://127.0.0.1/
```
