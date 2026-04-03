def find_path(graph, start, end):
    queue = [(start, [start])]  # (current node, path taken)
    visited = []

    while queue:
        node, path = queue.pop(0)  # FIFO

        if node == end:
            return True, path

        if node not in visited:
            visited.append(node)

            for neighbor in graph.get(node, []):
                queue.append((neighbor, path + [neighbor]))

    return False, []