import requests
response = requests.get('https://api.github.com')

if response:
    print("Get successful")
else:
    print("Get failure")