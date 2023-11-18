from django.shortcuts import render
from django.http import HttpResponse
import datetime
import re

from rest_framework.decorators import api_view
from rest_framework.response import Response
from test_job.settings import db


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
    if temp_list:
        temp_dict = temp_list[0]
        temp_dict.pop('_id')
    else:
        temp_dict = val.data_return
    return Response(temp_dict)
