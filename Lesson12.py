import requests

# Handling a bad number conversion
try:
    age = int("twenty six")
    print(age)
except ValueError:
    print("That's not a valid number!")

# Handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

# Handling an API call safely
try:
    response = requests.get("https://api.agify.io?name=natalie")
    response.raise_for_status()   # raises an error if the request failed
    data = response.json()
    print(f"API call succeeded: {data}")
except requests.exceptions.RequestException as e:
    print(f"API call failed: {e}")

print("Program finished without crashing!")