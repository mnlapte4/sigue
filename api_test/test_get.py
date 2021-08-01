import requests
import json

def test_get():
    url  = 'https://httpbin.org/get'
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(url, headers=headers)
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200

    resp_body = resp.json()
    assert resp_body['url'] == url

    # print response full body as text
    print(resp.text)
