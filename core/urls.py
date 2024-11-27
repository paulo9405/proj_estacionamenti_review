from django.conf.urls import url, include
from django.urls import path
from .views import home

urlpatterns = [
        #url(r'^$', home, name='core_home'), # chamo a função 'home' e dou o nome pra ela de 'core_home'
        path('index/', home, name='core_home')
]