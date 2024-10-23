
Graph = {
    'A': ['B', 'D'],
    'B': ['A','C','E'],
    'C': ['B', 'E'],
    'D': ['A', 'E'],
    'E': ['C','D']
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end= "")

        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

print("Przebieg przechodzenia po grafie przy uzyciu algorytmu BFS")
bfs(visited, Graph, 'D')