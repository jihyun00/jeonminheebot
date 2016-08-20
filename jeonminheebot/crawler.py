from contextlib import closing
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup


__all__ = 'request_html', 'parsing',


def request_html(url: str) -> str:
    with closing(urlopen(url)) as response:
        return response.read().decode('utf-8')


def parsing(html, class_name):
    result = {}
    soup = BeautifulSoup(html, 'html.parser')
    get_tags = soup.find_all('a', class_=re.compile('N=a:bls.title*'))

    title = get_tags[0].string.replace('\xa0', ' ')

    result['title'] = title
    result['href'] = get_tags[0].get('href')

    return result
