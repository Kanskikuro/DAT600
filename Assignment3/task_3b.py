from collections import defaultdict

def explore_paths(graph, current, reached, output=None):
    reached.add(current)
    for neighbor in graph[current]:
        if neighbor not in reached:
            explore_paths(graph, neighbor, reached, output)
    if output is not None:
        output.append(current)

def generate_reversed(graph):
    inverted = defaultdict(list)
    for vertex in graph:
        for adjacent in graph[vertex]:
            inverted[adjacent].append(vertex)
    return inverted

def capture_order(graph):
    visited = set()
    sequence = []
    for vertex in graph:
        if vertex not in visited:
            explore_paths(graph, vertex, visited, sequence)
    return sequence

def extract_scc(graph):
    completion_order = capture_order(graph)
    transposed = generate_reversed(graph)

    explored = set()
    components = []

    while completion_order:
        current = completion_order.pop()
        if current not in explored:
            cluster = []
            explore_paths(transposed, current, explored, cluster)
            components.append(cluster)

    return components

# Graph structure
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'A'],
    'C': ['E', 'F'],
    'D': ['C', 'B'],
    'E': ['G'],
    'F': ['E'],
    'G': ['F']
}


# Identify and display strongly connected components (groups)
groups = extract_scc(graph)
print("Groups:", groups)