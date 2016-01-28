from urllib.error import URLError

from pytest import mark, config, raises

from jeonminheebot.crawler import request_html, parsing, push_noti


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


@mark.parametrize('html, class_name', [
    ('''
    <html>
      <head></head>
      <body>
          <h1 id="id">hello world</h1>
          <div id="a">foo bar</div>
          <div class="nick">nyan</div>
          <div class="nick">minions</div>
      </body>
    </html>
    ''', 'nick'),
])
def test_parsing(html, class_name):
    assert parsing(html, class_name)
    assert parsing(html, class_name) == ['nyan', 'minions']


def test_push_noti():
    assert push_noti()
