import urllib.request,json


# Getting api key
api_key = None
# Getting the touristic base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['TOURISTIC_API_KEY']
    base_url = app.config['TOURISTIC_API_BASE_URL']


