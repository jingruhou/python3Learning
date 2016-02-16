import functools


def log(func):
    @functools.wraps(func)
    def wrape(*args, **kw):
        print('begin call')
        execute = func(*args, **kw)
        print('end call')
        return execute

    return wrape


@log
def now():
    print('2016-02-13')


now()
