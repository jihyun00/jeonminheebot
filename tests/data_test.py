@mark.parametrize('data', [
    ('http://naver.com/aaa'),
])
@real
def test_exist_data(data):
    assert exist_data(data)


def test_insert_data():
    assert insert_data()

