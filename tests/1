from urllib.error import URLError

from pytest import mark, config, raises

from jeonminheebot.crawler import request_html, parsing


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


@mark.parametrize('t, selector', [
    ('#id', 'hello world'),
    ('#a', 'foo bar'),
])
def test_parsing(t, selector):
    html = '''
    <html>
      <head></head>
      <body>
          <h1 id="id">hello world</h1>
          <div id="a">foo bar</div>
      </body>
    </html>
    '''
    assert parsing(html, selector)
    assert parsing(html, selector) == t

# 근데 왜 t랑 비교하지?
# parametrize랑 test_parsing이랑 비교하는 걸 만들어야 할 듯
