from contextlib import closing
from lxml.html import fromstring
from urllib.request import urlopen


def request_html(url: str) -> str:
    with closing(urlopen(url)) as response:
        return response.read().decode('utf-8')


def parsing(html, class_name):
    page = fromstring(html)
    get_tag = page.xpath('/html/body/ul/li/dl/dt/a')
    result = []
    get_attrib = {}

    for t in range(len(get_tag)):
        get_class = get_tag[t].get('class')

        if get_class.find(class_name) > -1:
            get_attrib['class'] = get_class
            get_attrib['href'] = get_tag[t].get('href')
            get_attrib['title'] = get_tag[t].text_content()
            result.append(get_attrib.copy())

    return result


def push_noti():
    return True
