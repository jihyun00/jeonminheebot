from contextlib import closing
from lxml.html import builder as E, fromstring
from urllib.request import urlopen


def request_html(url: str) -> str:
    with closing(urlopen(url)) as response:
        return response.read().decode('utf-8')


def parsing(html, tag) -> str:
    page = fromstring(html)
    text = page.get_element_by_id('a').text
    return text
    

def push_noti():
    return True
