from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()



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
        api_key = os.getenv('SECRET_KEY')
        headers = {'X-Api-Key': api_key}
        api_request = requests.get(api_url + str(query), headers=headers)
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'tracker.html', {'api': api})
    else:
        return render(request, 'tracker.html', {'query': 'Enter a valid query'})
