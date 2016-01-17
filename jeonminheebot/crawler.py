from contextlib import closing
from urllib.request import urlopen

from lxml import etree

def request_html(url: str) -> str:
    with closing(urlopen(url)) as response:
        return response.read().decode('utf-8')


def parsing(html, tag):
    # html 찾아서 tag 넣으면 selector를 return 
    return True


def open_db():
    conn = sqlite3.connect('jb.db')
    return True


def exist_data(html):
    return True


def insert_data():
    return True


def push_noti():
    return True


def close_db():
    return True
