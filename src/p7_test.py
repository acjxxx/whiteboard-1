from p7 import sqrt

print("Running square root test....")

print("Squareroot (4) = ", sqrt(4))
print("Squareroot (9) = ", sqrt(9))
print("Squareroot (16) = ", sqrt(16))
print("Squareroot (25) = ", sqrt(25))
print("Squareroot (36) = ", sqrt(36))

assert sqrt(4) == 2
assert sqrt(9) == 3
assert sqrt(16) == 4
assert sqrt(25) == 5
assert sqrt(36) == 6

print("Test p7 passed")