from p3 import gen_fib

result = gen_fib(10)
expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print("Running Fibonacci test....")
print("Result :", result)
print("Expected :", expected)

assert result == expected

print("Test P3 passed")