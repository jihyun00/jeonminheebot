from pync import Notifier


def noti(url):
    title = url.title
    href = url.href
    Notifier.notify(title, '나왔다고 전해라~',
                    open=href, title='전민희봇')
