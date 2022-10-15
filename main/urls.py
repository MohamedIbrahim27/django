from unicodedata import name
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='main'


urlpatterns = [
    path('',views.main_page),
    path('<str:slug>',views.main_detail,name='project_detail'),
    
]
