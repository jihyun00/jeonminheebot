from urllib.error import URLError

from pytest import config, mark, raises

from jeonminheebot.crawler import parsing, request_html


real = mark.skipif(not config.getoption('--real'), reason='--real')


@mark.parametrize('url, elem', [
    ('http://naver.com', '네이버'),
    ('http://daum.net', '다음'),
])
@real
def test_request_html(url, elem):
    response = request_html(url)
    assert elem in response


@real
def test_request_html_httperror():
    with raises(URLError):
        request_html('http://weofjwefoiwejfw.com')


def get_data():
    f = open('doc.txt', 'r')
    data = f.read()

    return data


@mark.parametrize('html, class_name', [
    (get_data(), 'N=a:bls.title'),
])
def test_parsing(html, class_name):
    data = get_data()
    assert parsing(data, class_name)
    assert parsing(data, class_name) == {
        'title': '세월의 돌 8',
        'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=9309138'}
