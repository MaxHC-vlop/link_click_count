import os
import json

from urllib.parse import urljoin, urlparse

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

    return response.json()['link']


def count_clicks(token, link):
    butly_prefix = 'v4/bitlinks/{0}/clicks/summary'
    url = urljoin(URL_TEMPLATE, butly_prefix.format(link))

    headers = {
        'Authorization': token,
        'bitlink': link,
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()

    return clicks_count['total_clicks']


def is_bitlink(token, url):
    link = urlparse(url)
    butly_prefix = f'/v4/bitlinks/{link.path}'
    url = urljoin(URL_TEMPLATE, butly_prefix)

    headers = {
        'Authorization': token,
    }

    response = requests.get(url, headers=headers)

    return response.ok


def main():
    user_input = input('Enter link: ')
    load_dotenv()
    token = os.getenv('API_TOKEN')
    try:
        response_status = is_bitlink(token, user_input)

        if response_status:
            return count_clicks(token, user_input)

        else:
            return shorten_link(token, user_input)

    except requests.exceptions.HTTPError as errh:
        exit("Can't get data from server:\n{0}".format(errh))

    except requests.exceptions.ConnectionError as errc:
        exit('Failed to connect to server:\n{0}'.format(errh))


if __name__ == '__main__':
    print(main())
