from . import views
from django.urls import path

app_name = 'demo'
urlpatterns = [
    path('', views.index, name='index'),
]
