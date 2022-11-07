from numpy import Inf
#create graph as adjacency list
graph2 = {
    0: [(1,1)],
    1: [(0,4),(2,5),(3,3)],
    2: [(1,2),(3,2),(4,7)],
    3: [(1,3),(2,6),(4,1)],
    4: [(2,5),(3,2)]
}
graphtest = {    
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]}
def dijikstras_algo(graph, root):
    n = len(graph)
    dist = [Inf for _ in range(n)]
    dist[root] = 0

    visited = [False for _ in range(n)]
    
    #loop through nodes
    for _ in range(n):
        #no starting node
        u = -1
        for i in range(n):
            # checks to see if i has not been visited and dist if dist is shorter than dist to start node
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == Inf:
            break
        visited[u] = True
        # compare distance to nodes from start node to currently known distance
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
    return dist

print(dijikstras_algo(graph2,1))