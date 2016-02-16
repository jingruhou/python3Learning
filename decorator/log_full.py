import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func._name_)
        return func(*args, **kw)

    return wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s $s():' % (text, func._name_))
            return func(*args, **kw)

        return wrapper

    return decorator()
