from p6 import max_occur

result = max_occur("Hello, world!")

print("Running Max Occurrence test...")
print("Result : ", result)
print("Expected : ('l', 3)")

assert result[0] == 'l'
assert result[1] == 3

print("Test P6 passed")