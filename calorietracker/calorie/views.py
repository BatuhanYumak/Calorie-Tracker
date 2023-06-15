from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()



def index(request):
    # Load the template named index.html
    template = loader.get_template('index.html')
    # Return the rendered template
    return HttpResponse(template.render())



def tracker(request):
    # Load the template named tracker.html
    template = loader.get_template('tracker.html')
    # Return the rendered template
    return HttpResponse(template.render())

def tracker(request):
    if request.method == 'POST':
        # Step 1: Retrieve the query from the POST request
        # Stap 1: Haal de query op uit het POST-verzoek

        query = request.POST.get('query', False)
        
        # Step 2: Prepare the API URL and headers
        # Stap 2: Bereid de API-URL en headers voor

        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_key = os.getenv('SECRET_KEY')
        headers = {'X-Api-Key': api_key}
        
        # Stap 3: Stuur het API-verzoek
        # Step 3: Send the API request
        api_request = requests.get(api_url + str(query), headers=headers)
        
        try:
            # Step 4: Parse the API response
            # Stap 4: Verwerk de API-reactie
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        
        # Stap 5: Render de 'tracker.html'-template met de API-gegevens
        # Step 5: Render the 'tracker.html' template with the API data
        return render(request, 'tracker.html', {'api': api})
    else:
                
        # Stap 6: Render de 'tracker.html'-template met een standaardbericht
        # Step 6: Render the 'tracker.html' template with a default message
        return render(request, 'tracker.html', {'query': 'Enter a valid query'})







