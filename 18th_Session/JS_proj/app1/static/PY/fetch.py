from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
import json

def fetch(URL):
    request = Request(URL)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    retItems = json.loads(response_body)
    return retItems