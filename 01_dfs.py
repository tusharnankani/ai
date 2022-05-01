visited = set()  

def dfs(visited, graph, node):  
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

print("Following is the Depth-First Search")
dfs(visited, graph, '5')

# 5 3 2 4 8 7

# graph2 = {
#     '0': ['1', '9'],
#     '1': ['2'],
#     '2': ['0', '3'],
#     '9': ['3'], 
#     '3': ['3']
# }

# print("\nFollowing is the Depth-First Search for graph 2")
# dfs(visited, graph2, '0')

# op2
# 0 1 2 3 9
