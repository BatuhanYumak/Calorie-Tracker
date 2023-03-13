from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def account(request):
    template = loader.get_template('account.html')
    return HttpResponse(template.render())

def tracker(request):
    template = loader.get_template('tracker.html')
    return HttpResponse(template.render())

    