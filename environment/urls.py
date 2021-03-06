from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'json/temperature/', views.json_temperature),
    url(r'json/humidity/', views.json_humidity),
    url(r'json/latest/', views.json_latest),
]
