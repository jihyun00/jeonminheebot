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
    assert parsing(data, class_name) == [
        {'title': '세월의 돌 8',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=9309138'},
        {'title': '세월의 돌 1',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=9309131'},
        {'title': '세월의 돌 2',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=9309132'},
        {'title': '세월의 돌 3',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=9309133'},
        {'title': '세월의 돌 4',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=9309134'},
        {'title': '세월의 돌 5',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=9309135'},
        {'title': '세월의 돌 7',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=9309137'},
        {'title': '세월의 돌 6',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=9309136'},
        {'title': '태양의탑 6',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=8778821'},
        {'title': '상속자들 하',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=7266654'},
        {'title': '상속자들 상',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=7097069'},
        {'title': '태양의 탑 5',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=6892706'},
        {'title': '전나무와 매',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=6692971'},
        {'title': 'ル-ンの子供たち 冬の劍(5)',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=6668025'},
        {'title': 'ル-ンの子供たち 冬の劍(4)',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=6621724'},
        {'title': '태양의 탑 4',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=6335073'},
        {'title': '태양의 탑 3',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=6242608'},
        {'title': '태양의 탑 1',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=6186935'},
        {'title': '태양의 탑 2',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=6186936'},
        {'title': '세월의 돌 7',
         'href': 'http://book.naver.com/bookdb/book_detail.nhn?bid=6012570'}
    ]
