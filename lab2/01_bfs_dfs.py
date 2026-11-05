from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def bfs(start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    return order

def dfs(start):
    visited = set()
    order = []

    def visit(node):
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbour in graph[node]:
            visit(neighbour)

    visit(start)
    return order

print("BFS:", bfs("A"))
print("DFS:", dfs("A"))
