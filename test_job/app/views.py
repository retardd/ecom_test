from django.shortcuts import render
from django.http import HttpResponse
import datetime
import re

from rest_framework.decorators import api_view
from rest_framework.response import Response
from test_job.settings import db, BASE_DIR
import os

import requests
import json


class Validator:
    regexes = {'data': r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$|^[0-9]{2}.[0-9]{2}.[0-9]{4}$',
               'email': r'^\S+@\w+.\w{2,4}$',
               'phone': r'^79\s*\d{2}\s*\d{3}\s*\d{2}\s*\d{2}$'}

    def __init__(self):
        self.data_return = {}

    def all_check(self, name, value):
        for key, rgx in self.regexes.items():
            res = False
            pattern = re.compile(rgx)
            if pattern.match(value):
                if key == 'data':
                    try:
                        res = bool(datetime.datetime.strptime(value, '%Y-%m-%d'))
                        self.data_return[name] = key
                        break
                    except ValueError:
                        try:
                            res = bool(datetime.datetime.strptime(value, '%d.%m.%Y'))
                            self.data_return[name] = key
                            break
                        except ValueError:
                            res = False
                else:
                    self.data_return[name] = key
                    res = True
                    break
        if res != True:
            self.data_return[name] = 'text'


@api_view(['GET', 'POST'])
def check_form(request):
    temp_dict = dict(request.GET.items())
    val = Validator()
    for name, value in temp_dict.items():
        val.all_check(name, value.strip())
    collect = db.forms_col
    temp_list = list(collect.find(val.data_return))
    print(temp_list)
    if temp_list:
        temp_dict = temp_list[0]
        temp_dict.pop('_id')
    else:
        temp_dict = val.data_return
    return Response(temp_dict)

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
