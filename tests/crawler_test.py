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
                     class="N:title;taetop">태양의 탑6</a>
                </dt>
                  <dd class="txt_block"></dd>
              </dl>
            </li>
            <li style="position:relative;">
              <div class="thumb type_search"></div>
              <dl>
                <dt>
                  <a href="http://naver.com/demonic" target="_blank"
                     class="N:title;demonic">룬의 아이들 데모닉</a>
                </dt>
                  <dd class="txt_block"></dd>
              </dl>
            </li>
            <li style="position:relative;">
              <div class="thumb type_search"></div>
              <dl>
                <dt>
                  <a href="http://naver.com/aaa" target="_blank"
                     class="N:error;stone">세월의 돌</a>
                </dt>
                  <dd class="txt_block"></dd>
              </dl>
            </li>
          </ul>
      </body>
    </html>
    ''', 'N:title'),
])
def test_parsing(html, class_name):
    assert parsing(html, class_name)
    assert parsing(html, class_name) == [{'classname': 'N:title;taetop',
                                          'href': 'http://naver.com/tower',
                                          'title': '태양의 탑6'},
                                         {'classname': 'N:title;demonic',
                                          'href': 'http://naver.com/demonic',
                                          'title': '룬의 아이들 데모닉'}]
