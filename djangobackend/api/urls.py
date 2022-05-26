from django.contrib import admin
from django.urls import path
from .views import home,search, login, fun, save_data

urlpatterns = [
    path('',fun),
    path('search/<str:item>/',search),
    path('send-data/', home),
    path('login/', login),
    path('save-data/',save_data)
]
