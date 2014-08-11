# Create your views here.

from django.http import HttpResponse
import datetime,time
from django.template import Template,Context
from django.template.loader import get_template
from models import Publisher
import sqlite3

def hello(request):
    # return HttpResponse(datetime.datetime.strptime(('%Y-%m-%d %H:%M:%S',datetime.datetime.time())))
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    t=get_template("mytemplete.html")
    html=t.render(Context({"person_name":now}))
    p=Publisher(name='Apress',
            address='2855 Telegraph Ave.',
            city='Berkeley',
            state_province='CA',
            country='U.S.A.',
            website='http://www.apress.com/')
    p.save()

    item_list=Publisher.objects.all()

    html=t.render(Context({"item_list":item_list}))
    return HttpResponse(html)