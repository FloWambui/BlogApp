from .import main
import urllib.request, json
from .models import Quote


base_url_random = 'http://quotes.stormconsultancy.co.uk/random.json'
def get_quote(random):
    get_quote_url = base_url_random.format(random)
    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None

        if get_quote_response:
            quote_results_list = get_quote_response
            quote_results = (quote_results_list)

    return quote_results



# Getting the popular quotes
base_url_popular = 'http://quotes.stormconsultancy.co.uk/popular.json'
def get_quotes(popular):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url_popular.format(popular)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response:
            quotes_results_list = get_quotes_response
            quotes_results = (quotes_results_list)

    return quotes_results


def process_results(quote_list):
    quotes_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        author = quote_item.get('author')
        quote = quote_item.get('quote')
        quote_object = Quote(id, author, quote)
        quotes_results.append(quote_object)

    return quotes_results

