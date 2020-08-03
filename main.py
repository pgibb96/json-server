import requests

url = "http://localhost:3000/people"

r = requests.get(url)

r_json = r.json()
print(r_json)
print("-------------")
print(r_json[0])
