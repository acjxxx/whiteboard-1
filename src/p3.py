def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def gen_fib(n):
    result = []
    for i in range(n):
        result.append(fib(i))
    return result
    