## Тестовое задание еКом

Docker + MongoDB (pymongo) + Django

/db/ - добавление новых записей в mongo

/get_form/?field_name=field_info&filed_name=filed_info... - GET-запрос (ответ реализован через DRF)

/start_test/ -  заполнить БД (перед этим коллекция дропается) и запустить тестовые запросы, ответ на которые выведется на странице
                тестовые запросы и тестовые формы можно поменять в app.views.start_test


Для запуска нужно ввести
    docker-compose build
    docker-compose up

И перейти на страницу http://127.0.0.1/