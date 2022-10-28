from django.http import HttpResponse
from django.shortcuts import render

from models_django.web.models import Employee


# Create your views here.

def index(request):
    # x = Employee.objects.all().filter(department_id=2)
    x = Employee.objects.all() \
        # .order_by('-age', 'first_name')
    # names_list = []
    #
    # for employee in x:
    #     names_list.append(employee.first_name)
    #
    # return HttpResponse(f"<html><body><h1>{', '.join(names_list)}</h1>.</body></html>")

    context = {
        'employees': x,
    }

    return render(request, 'index.html', context)


