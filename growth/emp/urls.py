from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.data),
    url(r'orderby=(?P<orderby>[\w]+)&limit=(?P<limit>[\w]+)&ordering=(?P<ordering>[\w]+)/',views.get)
]

#&limit=10&ordering=asc