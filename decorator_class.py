class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'num of calls is: {self.num_calls}')
        return self.func(*args, **kwargs)

@Count
def example():
    print('hello world')

example()

# output
# num of calls is: 1
# hello world

example()

# output
# num of calls is: 2
# hello world
