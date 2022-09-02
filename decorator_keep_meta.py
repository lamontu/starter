import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(message):
    print(message)

print(greet.__name__)

# 输出
#'greet'
