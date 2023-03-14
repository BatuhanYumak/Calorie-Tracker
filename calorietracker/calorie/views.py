from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import json
import requests


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def account(request):
    template = loader.get_template('account.html')
    return HttpResponse(template.render())

def tracker(request):
    template = loader.get_template('tracker.html')
    return HttpResponse(template.render())

def tracker(request):
    if request.method == 'POST':
        query = request.POST.get('query', False)
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
api_url + str(query), headers={'X-Api-Key': 'YOUR-API-KEY'})        
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'tracker.html', {'api': api})
    else:
        return render(request, 'tracker.html', {'query': 'Enter a valid query'})

    