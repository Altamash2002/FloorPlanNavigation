from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home ,name="home"),
    path('detail' , detail ,name="detail"),
    path('choose' , index ,name="index"),
    path('floor-navigate' , navigate ,name="navigate"),
    path('register' , register ,name="register"),
]