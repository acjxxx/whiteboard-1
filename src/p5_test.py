from p5 import sym_diff

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]

result = sym_diff(list1, list2)
expected = [1, 2, 3, 7, 8, 9]

print("Running symmetric difference test....")
print("Result :", sorted(result))
print("Expected : ", expected)

assert sorted(result) == expected

print("Test P5 passed")