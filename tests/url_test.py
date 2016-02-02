from jeonminheebot.url import Url


def test_create_url(f_session):
    href = 'http://naver.com'
    classname = 'tower'
    title = '태양의 탑'
    url = Url(href=href, classname=classname, title=title)
    f_session.add(url)
    f_session.commit()
    find_url = f_session.query(Url) \
                        .filter(Url.href == href) \
                        .first()
    assert find_url
    assert hasattr(find_url, 'href')
    assert find_url.href
    assert href == find_url.href
    assert hasattr(find_url, 'classname')
    assert hasattr(find_url, 'title')
    assert find_url.classname
    assert find_url.title
