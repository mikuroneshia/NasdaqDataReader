from django.contrib import admin
from django.urls import path,include
from Datareader.views import datareader,index,hundred,twohundred,graphmaker,test
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('admin/',datareader,name='admin'),
    path('form',index,name='form'),
    path('hundred',hundred,name='hundred'),
    path('twohundred',twohundred,name='twohundred'),
    path('graphmaker',graphmaker,name='graphmaker'),
    path('test',test,name='test')
    
]
