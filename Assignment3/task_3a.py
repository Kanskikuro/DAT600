from collections import defaultdict

def explore_paths(graph, current, reached):
    reached.add(current)
    for neighbor in graph[current]:
        if neighbor not in reached:
            explore_paths(graph, neighbor, reached)

def can_reach_all(graph, start):
    reached_nodes = set()
    explore_paths(graph, start, reached_nodes)
    return len(reached_nodes) == len(graph)

def detect_champions(graph):
    contenders = []
    for candidate in graph:
        if can_reach_all(graph, candidate):
            contenders.append(candidate)
    return contenders if contenders else "No champion exists."

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

# Identify and display champions
print("Champions:", detect_champions(graph))