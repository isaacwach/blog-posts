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

