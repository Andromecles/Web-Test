import requests
response = requests.get('https://api.github.com', params={'q': 'requests+language:python'},)

if response:
    for thing in response.json():
        print(thing)
    print("Get successful")
else:
    print("Get failure")