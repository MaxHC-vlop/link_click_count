import argparse
import os
import logging

from urllib.parse import urljoin, urlparse

import requests

from dotenv import load_dotenv


URL_TEMPLATE = 'https://api-ssl.bitly.com/v4/bitlinks/'


def shorten_link(token, user_args):
    headers = {
        'Authorization': token,
    }
    payload = {
        'long_url': user_args,
    }

    response = requests.post(URL_TEMPLATE, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(token, user_args):
    link = urlparse(user_args)
    url_prefix = f'{link.netloc}{link.path}/clicks/summary/'
    url = urljoin(URL_TEMPLATE, url_prefix)

    headers = {
        'Authorization': token
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()

    return clicks_count['total_clicks']


def is_bitlink(token, url):
    link = urlparse(url)
    url_prefix = f'{link.netloc}{link.path}'
    url = urljoin(URL_TEMPLATE, url_prefix)

    headers = {
        'Authorization': token,
    }

    response = requests.get(url, headers=headers)

    return response.ok


def main():
    parser = argparse.ArgumentParser(
        description='Chek is bitlink'
    )
    parser.add_argument('link', type=str)

    args = parser.parse_args()

    load_dotenv()
    token = os.environ.get('BITLY_TOKEN')
    
    logging.basicConfig(format={} ,level=logging.INFO)
    try:
        if is_bitlink(token, args.link):
            logging.info(f'Number of hits on the bitlink: {count_clicks(token, args.link)}')

        else:
            logging.info(f'Your new bitlink: {shorten_link(token, args.link)}')

    except requests.exceptions.HTTPError as errh:
        logging.error("Can't get data from server:\n{0}".format(errh))

    except requests.exceptions.ConnectionError as errc:
        logging.error('Failed to connect to server:\n{0}'.format(errc))


if __name__ == '__main__':
    main()
