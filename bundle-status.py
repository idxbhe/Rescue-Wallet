import requests

# Replace these with your actual values
BLOXROUTE_AUTH_HEADER = 'AUTH HEADER HERE'
BUNDLE_HASH = 'BUNDLE HASH'


url = f'https://tools.bloxroute.com/bscbundletrace/{BUNDLE_HASH}'
headers = {
    'Content-Type': 'application/json',
    'Authorization': BLOXROUTE_AUTH_HEADER
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f'Error: {response.status_code}')
    print(response.text)
