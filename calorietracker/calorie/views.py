from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def calorie (args):
#     return HttpResponse("This is the calorie page.")

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())