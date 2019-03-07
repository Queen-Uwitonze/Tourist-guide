import urllib.request,json
from .models import Map


import urllib.request,json
from .models import Map

# Getting api key
api_key = None
# Getting the Map base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['Map_API_KEY']
    base_url = app.config['Map_API_BASE_URL']



