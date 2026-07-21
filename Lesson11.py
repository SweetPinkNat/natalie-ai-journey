import requests

# Ask an API to guess an age based on a name
response = requests.get("https://api.agify.io?name=natalie")

if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['name']}")
    print(f"Predicted age: {data['age']}")
    print(f"Based on {data['count']} data points")
else:
    print(f"Something went wrong: {response.status_code}")
    