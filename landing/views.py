from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class FirstClass(TemplateView):
    template_name = 'landing/first.html'