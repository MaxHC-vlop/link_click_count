import os
import json

from urllib.parse import urljoin

import requests

from dotenv import load_dotenv


URL_TEMPLATE = 'https://api-ssl.bitly.com'

def main():
    butly_prefix = '/v4/bitlinks'
    url = urljoin(URL_TEMPLATE, butly_prefix)
    print(url)
    load_dotenv()
    token = os.getenv('TOKEN')

    headers = {
        'Authorization': token,
    }

    payload = {
        'long_url': 'https://python-scripts.com/json',
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print(response.json())


if __name__ == '__main__':
    main()