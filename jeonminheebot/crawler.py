from contextlib import closing
from lxml.html import fromstring
from urllib.request import urlopen


def request_html(url: str) -> str:
    with closing(urlopen(url)) as response:
        return response.read().decode('utf-8')


def parsing(html, class_name) -> str:
    page = fromstring(html)
    get_class = page.find_class(class_name)
    name = [e.text for e in get_class]
    return name

    # def blah blah... 함수 만들기 -> get_class 
    # list의 len이 하나 이상일 경우 처리하는 테스트


def push_noti():
    return True
