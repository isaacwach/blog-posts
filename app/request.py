import urllib.request, json
from .models import Quote

def configure_request(app):
    global quote_url 
    quote_url = app.config['QUOTES_API_BASE_URL']

def get_source():
    get_source_url = quote_url()
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response=json.loads(get_sources_data)

        source_results=None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):

    source_results = []
    for source_item in source_list:
        id= source_item.get('id')
        author= source_item.get('author')
        quote= source_item.get('quote')
        permalink = source_item.get('permalink')
        if id:
            source_object=Source(id,author, quote, permalink)
            source_results.append(source_object)

    return source_results