from django.urls import path
from polls.views import index, ola

urlpatterns = [
    path('index/', ola, name='index'),

    path('ola/', ola, name='ola')
]