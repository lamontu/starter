
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

# add this decorator to decrease the call count
@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res


import cProfile
cProfile.run('fib_seq(30)')
