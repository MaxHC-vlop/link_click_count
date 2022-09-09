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


def count_clicks(token, link):
    butly_prefix = 'v4/bitlinks/{0}/clicks/summary'
    url = urljoin(URL_TEMPLATE, butly_prefix.format(link))

    headers = {
        'Authorization': token,
        'bitlink': link,
    }
    # payload = {
    #     'bitlink': link,
    # }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()

    return clicks_count['total_clicks']


def main():
    user_input = input()

    load_dotenv()
    token = os.getenv('TOKEN')
    try:
        link = shorten_link(token, user_input)['id']
        print(link)
        count = count_clicks(token, link)
        print(count)
    except requests.exceptions.HTTPError as errh:
        exit("Can't get data from server:\n{0}".format(errh))


if __name__ == '__main__':
    main()
