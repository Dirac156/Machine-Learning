import requests
import json

def correlate_person_title(person: str):
    """ """

    person2 = person.split(" ")

    url = "https://api.genderize.io?name=" + person2[0]

    headers = {'Content-type': 'json'}

    response = requests.get(url, headers=headers)

    json_response = json.loads(response.text)

    if (json_response.get('gender') == "male"):
        return 'Mr. ' + person.capitalize()
    else:
        return 'Ms. ' + person.capitalize()
