import json
import urllib3

def hello(event, context):
    http = urllib3.PoolManager()
    url = "https://api.thecatapi.com/v1/images/search"
    r = http.request('GET', url)
    data = json.loads(r.data.decode('utf-8'))
    
    body = "<html><body><h1>Coucou !</h1><p>bonjour!</p><img src='" +data[0]['url'] + "'/></body></html>"


    return body


