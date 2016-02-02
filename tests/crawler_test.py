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
          <ul class="basic" id="searchBiblioList" style="position:relative;">
            <li style="position:relative;">
              <div class="thumb type_search"></div>
              <dl>
                <dt>
                  <a href="http://naver.com/tower" target="_blank"
                          class="taetop">태양의 탑6</a>
                </dt>
                  <dd class="txt_block"></dd>
              </dl>
            </li>
            <li style="position:relative;">
              <div class="thumb type_search"></div>
              <dl>
                <dt>
                  <a href="http://naver.com/demonic" target="_blank"
                          class="demonic">룬의 아이들 데모닉</a>
                </dt>
                  <dd class="txt_block"></dd>
              </dl>
            </li>
          </ul>
      </body>
    </html>
    ''', 'N=a:bls.title'),
])
def test_parsing(html, class_name):
    assert parsing(html, class_name)
    assert parsing(html, class_name) == [{'class': 'taetop',
                                          'href': 'http://naver.com/tower',
                                          'title': '태양의 탑6'},
                                         {'class': 'demonic',
                                          'href': 'http://naver.com/demonic',
                                          'title': '룬의 아이들 데모닉'}]


def test_push_noti():
    assert push_noti()
