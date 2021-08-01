import requests
import json

def test_delete():
    url  = 'https://httpbin.org/anything'
    headers = {'Content-Type': 'application/json' }
    resp = requests.put(url, headers=headers)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    #assert resp.status_code == 201
    resp_body = resp.json()
    assert resp_body['url'] == url
    
    # print response full body as text
    print(resp.text)