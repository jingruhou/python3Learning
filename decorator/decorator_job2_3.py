import functools


def log(arg):
    def decorator(func=arg):
        text = 'call' if func == arg else arg

        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return (func(*args, **kw), print('end %s %s():' % (text, func.__name__)))[0]

        return wrapper

    return decorator() if callable(arg) else decorator


@log
def now():
    print('2016-02-13: 1')

now()


@log('execute')
def now1():
    print('2016-02-13: 2')

now1()
