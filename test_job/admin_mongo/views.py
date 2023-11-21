from django.shortcuts import render
from django.http import HttpResponse
from test_job.settings import db


def add_templates(request):
    if request.method == 'POST':
        temp_dict = dict(request.POST.items())
        dict_to_db = {"name": temp_dict["main"]}
        temp_key = ""
        for key, value in temp_dict.items():
            if "input" in key:
                if temp_key == "":
                    temp_key = key
                else:
                    temp_type = temp_dict[key]
                    if temp_type in ['email', 'text', 'phone', 'data']:
                        dict_to_db[temp_dict[temp_key]] = temp_type
                    else:
                        dict_to_db[temp_dict[temp_key]] = 'text'
                    temp_key = ""
        collect = db.forms_col
        print(dict_to_db)
        collect.insert_one(dict_to_db)
    return render(request, 'admin.html')
