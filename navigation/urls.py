from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , detail ,name="detail"),
    path('choose' , home ,name="home"),
    path('floor-navigate' , navigate ,name="navigate"),
    path('register' , register ,name="register"),
]