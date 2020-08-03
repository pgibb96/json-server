import requests

url = "http://localhost:3000/people"

r = requests.get(url)

if r.status_code != 200:
    sys.exit("GET error")

r_json = r.json()

def build_likes(r_json):
    dictionary = {}
    for person in r_json:
        add_interest(person, dictionary)
    return dictionary

def add_interest(person, dictionary):
    for interest in person['interests']:
        # Storing list of people who have this interest
        if interest not in dictionary:
            dictionary[interest] = []
        dictionary[interest].append(person['name'])
