import requests

data = {'search': 'hello world?'}

r = requests.post('http://localhost:8000/post', json=data)
print('status:', r.status_code)
print('json:', r.json())