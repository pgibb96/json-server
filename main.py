import requests

url = "http://localhost:3000/posts/1"

r = requests.get(url)

r_json = r.json()

def format(r_json):
    print("ID: " + str(r_json['id']))
    print("Title: " + str(r_json['title']))
    print("Author: " + str(r_json['author']))

format(r_json)
