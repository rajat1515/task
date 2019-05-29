from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import json
#from django.views.generic import View
from django.core.serializers import serialize
from emp.models import Emp

def data(request):
    return HttpResponse('<h1>data</h1>')


def get(request, orderby,limit,ordering=None):
    if request.method != 'GET':
        return HttpResponse('<h1>invalid request</h1>')

    if request.method == 'GET':
        limit = int(limit)
        if ordering == 'asc':
            em = Emp.objects.all().order_by(orderby)[:limit]
            emp_data = serialize('json', em)
            return HttpResponse(emp_data, content_type='application/json')

        elif ordering == 'desc':
            em = Emp.objects.all().order_by(-orderby)[:limit]
            emp_data = serialize('json', em)
            return HttpResponse(emp_data, content_type='application/json')



'''
class data_CSV(View):
    def get(self,request,orderby,*args,**kwargs):
        em=Emp.objects.all().order_by(orderby)
        #data={'emp_n':em.emp_no, 'emp_nam':em.emp_name}
        #emp_data=json.dumps(data)
        emp_data=serialize('json',em)
        return HttpResponse(emp_data,content_type='application/json')
'''