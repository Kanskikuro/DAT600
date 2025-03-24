from itertools import combinations

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

def kruskal_mst(edges, n):
    uf = UnionFind(n)
    mst_cost = 0
    edges.sort(key=lambda x: x[2])

    mst_edges = []

    for u, v, cost in edges:
        if uf.union(u, v):
            mst_cost += cost
            mst_edges.append((u, v, cost))

    if len(mst_edges) == n - 1:
        return mst_cost
    else:
        return float('inf')

def kruskal_mst_with_constraint(edges, n, restricted_node, max_degree):
    uf = UnionFind(n)
    mst_cost = 0
    edges.sort(key=lambda x: x[2])

    degree_count = [0] * n
    mst_edges = []

    for u, v, cost in edges:
        if (u == restricted_node or v == restricted_node):
            if degree_count[restricted_node] >= max_degree:
                continue

        if uf.union(u, v):
            mst_cost += cost
            mst_edges.append((u, v, cost))
            degree_count[u] += 1
            degree_count[v] += 1

    if len(mst_edges) == n - 1:
        return mst_cost
    else:
        return float('inf')  # Return infinite cost if MST is not possible

def find_valid_swap(edges, vertices, budget):
    for (i, j) in combinations(range(len(edges)), 2):
        new_edges = edges[:]

        # Swap edge costs
        (u1, v1, c1), (u2, v2, c2) = new_edges[i], new_edges[j]
        new_edges[i] = (u1, v1, c2)
        new_edges[j] = (u2, v2, c1)

        mst_cost = kruskal_mst(new_edges, vertices)
        if mst_cost <= budget:
            return new_edges[i], new_edges[j], mst_cost

    return None, None, float('inf')

# Graph vertices and edges
vertices = 8
# A = 0, B = 1, C = 2, D = 3, E = 4, F = 5, G = 6, H = 7
edges = [
    (0, 1, 5), (0, 3, 1), (1, 3, 4), (3, 2, 2), (3, 4, 2),
    (2, 6, 6), (4, 5, 8), (5, 7, 7), (6, 5, 9), (1, 7, 8), (3, 5, 4)
]

budget = 30
budget_c = 25

restricted_node = 3
max_degree = 3
mst_cost = kruskal_mst(edges, vertices)
mst_cost_constraint = kruskal_mst_with_constraint(edges, vertices, restricted_node, max_degree)

swap1, swap2, new_cost = find_valid_swap(edges, vertices, budget_c)

print("Total cost of Minimum Spanning Tree:", mst_cost)
if mst_cost <= budget:
    print("Yes, it's possible to connect all neighborhoods within the budget.")
else:
    print("No, it's NOT possible to connect all neighborhoods within the budget.")
print("##############################################")

print("Total cost of constrained MST:", mst_cost_constraint)
if mst_cost_constraint <= budget:
    print("Yes, it's possible to connect all neighborhoods within the budget with the degree constraint.")
else:
    print("No, it's NOT possible to connect all neighborhoods within the budget with the degree constraint.")
print("##############################################")

if new_cost <= budget_c:
    print("Valid swap found:", swap1, "<->", swap2)
    print("New MST cost:", new_cost)
else:
    print("No valid swap found that meets the budget constraint.")

