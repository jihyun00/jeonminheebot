from contextlib import closing
from urllib.request import urlopen


def request_html(url: str) -> str:
    with closing(urlopen(url)) as response:
        return response.read().decode('utf-8')


def parsing(html, selector):
    return True
