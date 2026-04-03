from p2 import fizzbuzz

result = fizzbuzz()

print("Running test...")
print("Results: ", result[:100])

assert result[2] == "Fizz"
assert result[4] == "Buzz"
assert result[14] == "FizzBuzz"

print("Test P2 passed")