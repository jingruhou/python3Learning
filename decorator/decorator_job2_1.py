def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('begin call')
            print('%s : %s' % (text, func.__name__))
            execute = func(*args, **kw)
            print('end call')
            return execute
        return wrapper
    if isinstance(text, str):
        return decorator

    func = text
    text = 'execute'
    return decorator(func)


@log('execute')
def now():
    print('2016-02-13')


now()
