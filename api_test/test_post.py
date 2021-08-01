
import requests
import json

def test_post():
    url     = 'https://httpbin.org/post'
    headers = {'Content-Type': 'application/json' } 

    # Body
    body = {'key1': 1, 'key2': 'value2'}
    resp = requests.post(url, headers=headers, data=json.dumps(body,indent=4))       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    #assert resp.status_code == 201
    resp_body = resp.json()
    assert resp_body['url'] == url
    
    # print response full body as text
    print(resp.text)