import numpy as np

def bfs(graph, node):
    visited = []
    visited.append(node)
    queue.append(node)

    while queue:
        nodes = queue.pop(0)

        for neighbour in graph[nodes]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                edges.append("{}-{}".format(nodes, neighbour))
    return visited

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                edges.append("{}-{}".format(node, neighbour))
                dfs(visited, graph, neighbour)
    return visited


txt = open('in2.txt', "r").read()
N = txt[0]
n = int(N)
matrix = np.loadtxt('in2.txt', dtype=int, skiprows=1, usecols=range(n))
print(matrix)

graph = {}
for i in range(n):
    lista = []
    for j in range(n):
        if (matrix[i][j] == 1):
            lista.append(j)
    graph.update({i: lista})
print(graph)
print()
queue = []
edges = []
print("Wierzchołki wg odwiedzenia BFS: ", bfs(graph, 0))
print("Krawędzie: ", edges)
print()
visited = []
edges = []
print("Wierzchołki wg odwiedzenia BFS: ", dfs(visited, graph, 0))
print("Krawędzie: ", edges)




