import os
import json

from urllib.parse import urljoin

import requests

from dotenv import load_dotenv


URL_TEMPLATE = 'https://api-ssl.bitly.com'


def shorten_link(token, user_input):
    butly_prefix = '/v4/bitlinks'
    url = urljoin(URL_TEMPLATE, butly_prefix)

    headers = {
        'Authorization': token,
    }
    payload = {
        'long_url': user_input,
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()


def main():
    user_input = input()

    load_dotenv()
    token = os.getenv('TOKEN')

    print('Битлинк', shorten_link(token, user_input)['link'])


if __name__ == '__main__':
    main()
