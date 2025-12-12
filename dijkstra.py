
adjacent_list = {}
arr = [float('inf')]*len(list(adjacent_list.keys()))
visited = set()
total_cost = 0

def dijkstra(source, dest, cost, adj):
    if source == dest:
        return
    arr[source] = cost+adj[]
    visited.add(source)
    for i in adj[source]:
        if i not in visited:
            if dijkstra(i, dest, cost, )


dijkstra(0, 6, 0, adjacent_list)

'''
adjacency_list = {0: [[1, 3], [2, 2]],
                  1: [[0, 3], [5, 2]],
                  2: [[0, 2], [5, 1]],
                  3: [[2, 4], [4, 2], [6, 2]],
                  4: [[5, 2], [3, 2]],
                  5: [[1, 2], [2, 1], [4, 2], [6, 2]],
                  6: [[5, 2], [4, 1], [3, 2]]
                    }

'''