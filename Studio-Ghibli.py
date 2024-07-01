import requests

# base url
base_url = 'https://ghibliapi.vercel.app'

endpoint = '/films'
url = base_url + endpoint

#Sending get requests
response = requests.get(url)

if response.status_code == 200:
  print(response.json())
else:
  print(f"Failed to retrieve data. Status code: {response.status_code}")
