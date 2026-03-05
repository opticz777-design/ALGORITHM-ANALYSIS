from collections import deque, defaultdict

# Define DAG using adjacency list
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

# -------------------------------
# Method A: Kahn's Algorithm (BFS)
# -------------------------------
def kahn_topological_sort(graph):
    in_degree = {u: 0 for u in graph}

    # Calculate in-degrees
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Collect nodes with in-degree 0 (sorted for deterministic output)
    queue = deque(sorted([u for u in graph if in_degree[u] == 0]))

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in sorted(graph[node]):  # deterministic neighbor order
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

        queue = deque(sorted(queue))  # maintain alphabetical order

    return topo_order


# ----------------------------------
# Method B: DFS-Based Topological Sort
# ----------------------------------
def dfs_topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in sorted(graph[node]):  # deterministic order
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in sorted(graph):  # ensure deterministic start
        if node not in visited:
            dfs(node)

    stack.reverse()
    return stack


# Run both methods
kahn_result = kahn_topological_sort(graph)
dfs_result = dfs_topological_sort(graph)

# Display results
print("Topological Sort using Kahn's Algorithm:")
print(" -> ".join(kahn_result))

print("\nTopological Sort using DFS:")
print(" -> ".join(dfs_result))

# Save results to file
with open("topological_sort_results.txt", "w") as file:
    file.write("Topological Sorting Results\n")
    file.write("---------------------------\n")
    file.write("Kahn's Algorithm: " + " -> ".join(kahn_result) + "\n")
    file.write("DFS-Based Algorithm: " + " -> ".join(dfs_result) + "\n")
