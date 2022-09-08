import os

import requests

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
url = 'https://api-ssl.bitly.com/v4/user'
headers = {
    "Authorization":token
}

response = requests.get(url, headers=headers)
response.raise_for_status()
print(response.text)