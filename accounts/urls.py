from django.contrib import admin
from django.template.backends import django
from django.urls import path, include
from . import views

urlpatterns = [

    path('signup/', views.SignUpView.as_view(), name='signup'),

]
