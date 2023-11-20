# Тестовое задание еКом

### Docker + MongoDB (pymongo) + Django

1. Рабочие страницы
    [/db/](http://127.0.0.1/db/) - добавление новых записей в mongo

    [/get_form/?field_name=field_info...](http://127.0.0.1/get_form/?field_name=field_info) - GET-запрос (ответ реализован через DRF)

    [/start_test/](http://127.0.0.1/start_test/) - заполнить БД (перед этим коллекция дропается) и запустить тестовые запросы, ответ на которые выведется на странице
                тестовые запросы и тестовые формы можно поменять в app.views.start_test 
    
   
2. Тестовые шаблоны и запросы выглядят следующим образом: 
    ```py
   
    def start_test(request):
    list_dicts = [{"name": "yor_mails", "mail1": "email", "mail2": "email", "mail3": "email"},
                  {"name": "only_phone", "phone": "phone"},
                  {"name": "full_info", "name_user": "text", "surname": "text", "mail": "email", "phone": "phone"},
                  {"name": "two_text", "text_1": "text", "text_2": "text"},
                  {"name": "mail", "mail": "email"}]

    collect = db.forms_col
    collect.drop()
    collect.insert_many(list_dicts)

    list_urls = ["http://127.0.0.1:8000/get_form/?mail1=ryazantsev@ya.ru&mail2=ryazantsev@ya.ru&mail3=ryazantsev@ya.ru",
                 "http://127.0.0.1:8000/get_form/?mail=iovryz@grn.ru",
                 "http://127.0.0.1:8000/get_form/?phone=+79518681525&text_filed=text",
                 "http://127.0.0.1:8000/get_form/?phone=+79518681525",
                 "http://127.0.0.1:8000/get_form/?phone=+79518681525&example_filed=text",
                 "http://127.0.0.1:8000/get_form/?name_user=text&surname=text&mail=ryazantsev@mail.ru&phone=+79867612323"]

    json_ = []


    for url in list_urls:
        json_.append("ЗАПРОС: {}<br>ОТВЕТ: {}".format(url, requests.get(url=url).text))


    return HttpResponse("<br><br>".join(json_))


3. Деплой
    - `docker-compose build`
    - `docker-compose up`
    - И перейти на страницу http://127.0.0.1/start_test