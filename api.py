import requests

# 1
# r = requests.get('https://api.github.com/users/pipusana')
# print(r.json()['login'])

#2
token = 'EAAIFzgWqZBfABAIbKnMKdstuZAMLiZCeVlTl10sGjNZAZAo503hr5EqscDzrGxVo8ekPgsduvdSlV2QsX1ZC185Pa0PSMf6MjK7hmnSbKwd1WswZA9ZCNslewA177AbCFMiNJPtZBa0Bk5xKhXJW3AIXN9zCGlPjNHdimD16'
url = 'https://graph.facebook.com/v3.1/me'
payload = {'fields': 'id,name,birthday', 'access_token': token}
r = requests.get(url, params=payload)
print(r.json()['name'])