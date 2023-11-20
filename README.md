# Тестовое задание еКом

### Docker + MongoDB (pymongo) + Django

/db/ - <i> добавление новых записей в mongo </i>

/get_form/?field_name=field_info&filed_name=filed_info... - <i> GET-запрос (ответ реализован через DRF) </i>

/start_test/ - <i> заполнить БД (перед этим коллекция дропается) и запустить тестовые запросы, ответ на которые выведется на странице
                тестовые запросы и тестовые формы можно поменять в app.views.start_test </i> 


Для запуска нужно ввести
    : docker-compose build \
    docker-compose up

И перейти на страницу http://127.0.0.1/