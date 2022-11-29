from django.urls import path
from .import views

urlpatterns=[
    path('', views.FirstClass.as_view(), name='home')
]