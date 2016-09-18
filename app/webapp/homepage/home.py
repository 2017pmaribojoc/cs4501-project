from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import os


def index(request):
    template = loader.get_template('sample_homepage/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def index2(request):
    template = loader.get_template('homepage/index.html')
    context = {
        'name': "Patrick"
    }

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    return HttpResponse(template.render(context, request))