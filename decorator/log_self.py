def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2016-02-13')

now()


