graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['G', 'A'],
    'D': ['A', 'H'],
    'E': ['B'],
    'F': ['B'],
    'G': ['C'],
    'H': ['D']
}

visited = set()
par = {}

def dfs(node, parent, curDepth, maxDepth, endNode, graph, visited):
    if(curDepth > maxDepth):
        return

    par[node] = parent
    visited.add(node)

    if(node == endNode):
        return

    for x in graph[node]:
        if x not in visited:
            dfs(x, node, curDepth+1, maxDepth, endNode, graph, visited)


def iterativeDfs(startNode, endNode, maxDepth):
    for i in range(maxDepth+1):
        for x in graph:
            par[x] = '#'
        visited.clear()

        dfs(startNode, par[startNode], 0, i, endNode, graph, visited)

        if par[endNode] != '#':
            print("\nPath found :", end=' ')
            ans = []
            while endNode != '#':
                ans.append(endNode)
                endNode = par[endNode]

            ans.reverse()
            print(ans)
            break


startNode = input("Enter the start node : ")
endNode = input("Enter the goal node : ")
maxDepth = int(input("Enter the max depth : "))

iterativeDfs(startNode, endNode, maxDepth)

if par[endNode] == '#':
    print("\nGoal node not found ")