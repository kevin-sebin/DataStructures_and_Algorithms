def dfs(node, visited, graph):
    print(node)
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, visited, graph)


def detectCycle(ele, parent, visited, graph):
    visited.add(ele)
    for nei in graph[ele]:
        if nei not in visited:
            if detectCycle(nei, ele, visited, graph):
                return True
        elif nei != parent:
            return True
    return False


def bfs(start, graph):
    visited = set()
    queue = []
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(node)
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
    return visited


graph = {
    0: [1, 2],
    1: [0, 2, 4],
    2: [0, 1, 3],
    3: [2],
    4: [1]
}

start = 3

# DFS
visited = set()
print(dfs(start, visited, graph))

# BFS
print(bfs(start, graph))            

# Cycle detection
visited_cycle = set()
print(detectCycle(start, -1, visited_cycle, graph))
