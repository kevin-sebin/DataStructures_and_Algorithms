
visited = set()
def dfs(ele, s):
    visited.add(ele)
    if ele == s:
        return True
    for i in graph[ele]:
        if i not in visited:
            return dfs(i, s)
    return False

def detectCycle(ele, p):
    if ele in visited and ele != p:
        return True
    else:
        visited.add(ele)
        for i in graph[ele]:
            if i != p:
                return detectCycle(i, ele)
        return False
        
graph = {
    0: [1, 2],
    1: [0, 2, 4],
    2: [0, 1, 3],
    3: [2], 
    4: [1]
}
start = 3
# print(dfs(start, 3))
print(detectCycle(start, -1))


    