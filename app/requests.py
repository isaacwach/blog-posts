import requests,json
import time

url = 'http://quotes.stormconsultancy.co.uk/random.json'   
page = requests.get(url, verify=False)

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    #if response.status_code == 200:
    quote = response.json()
    return quote