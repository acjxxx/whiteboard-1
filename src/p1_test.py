from p1 import insertion_sort

def run_test(test_name, result, expected):
    print(f"Running {test_name}...")
    print("Result:   ", result)
    print("Expected: ", expected)
    assert result == expected
    print("Test P1 passed\n")

data = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]
expected = [-36, -16, -3, 8, 21, 28, 55, 77, 99, 111, 400]

run_test("Sorting Test", insertion_sort(data), expected)