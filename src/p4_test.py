from p4 import intersection

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]

result = intersection(list1, list2)
expected = [4, 5, 6]

print("Running intersection test....")
print("Result : ", sorted(result))
print("Expected :", expected)

assert sorted(result) == expected

print("Test p4 passed")