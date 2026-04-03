from p9 import find_path

graph = {
    'A': [],
    'B': ['A', 'D'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': ['B'],
    'G': []
}

print("Running Graph Path Test...")

print("D -> B:", find_path(graph, 'D', 'B'))
print("F -> A:", find_path(graph, 'F', 'A'))
print("G -> C:", find_path(graph, 'G', 'C'))
print("E -> D:", find_path(graph, 'E', 'D'))


assert find_path(graph, 'D', 'B')[0] == False
assert find_path(graph, 'F', 'A')[0] == True
assert find_path(graph, 'G', 'C')[0] == False
assert find_path(graph, 'E', 'D')[0] == True


print("Test p9 passed\n")