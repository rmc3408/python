import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')
result = r.json()
print()