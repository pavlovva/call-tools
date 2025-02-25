# Задание на Middle Python Developer

### 1. Какой опыт в коммерческой разработке на Python?
- 5 лет

### 2. Приходилось ли сильно оптимизировать Python код? Какие подходы и инструменты для этого использовали?
- Да, приходилось. Использовал профайлеры `cProfile` и `timeit`, чтобы находить узкие места. Убирал лишние вычисления, кешировал результаты, добавлял асинхронный подход.

### 3.
**a)** Какие из этих фреймворков Django, Flask, FastAPI вы использовали в работе?
- Все. Больше всего опыта с Django.

**б)** Какой опыт работы с ними? Дайте оценку своему уровню знаний фреймворка.
- Django — все 5 лет, Flask и FastAPI — 1 год.  
  - Django — 8/10  
  - Flask, FastAPI — 6/10

### 4. Какие брокеры сообщений использовали в работе (RabbitMQ, Kafka и т.д.)?
- Использовал RabbitMQ

### 5. 
**a)** Работали ли ранее с SQL (чистые запросы, ORM)? Какие ORM использовали?
- Работал с SQL как с чистыми запросами, так и через ORM. Основной опыт с Django ORM и SQLAlchemy.

**б)** Какие СУБД использовали в работе (SQLite, PostgreSQL, MySQL, MongoDB, ClickHouse и др.)?
- Основной опыт работы с PostgreSQL. С MongoDB был небольшой опыт.

**в)** Каков максимальный размер БД, с которой был опыт работы?
- На последнем проекте около 500 ГБ на PostgreSQL и порядка 4 ТБ на MongoDB.

### 6. Есть ли еще какой-то интересный вам язык программирования, который используете, и какие задачи предпочитаете на нем решать?
- Использую Bash в работе с продуктами Virtuozzo.

### 7. Задача на подумать:

Есть веб-сервис А, принимающий запросы от пользователей, запросов может приходить в час до 200 000. В день — до 2 000 000 запросов.  
Сервис А должен отправить эти данные в сервис Б, чтобы обработать данные.  
Сервис Б может обработать 100 000 запросов в час.  
Запросы от пользователей, поступающие в сервис А, нельзя потерять.  

**Как бы вы организовали межсервисное взаимодействие, хранение данных, результаты, и какие инструменты использовали бы для этого?**

- Сервис А принимает запрос.
- Сервис А сохраняет запрос в БД (например, MongoDB), которая может быть частью сервиса А или отдельным инстансом (предпочтительно).
- Сервис А передает запрос в RabbitMQ.
- Сервис Б подписан на очередь RabbitMQ, читает запросы и обрабатывает их.
- Запись удаляется из базы данных после успешной обработки или по крону раз в какое-то время.