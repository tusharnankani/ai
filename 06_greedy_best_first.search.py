graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('C', 4), ('D', 1)],
    'B': [('E', 3), ('F', 1)],
    'E': [('H', 5)],
    'F': [('I', 2), ('G', 3)],
    'C': [('A', 4)],
    'D': [('A', 1)],
    'E': [('B', 3)],
    'I': [('F', 2)],
    'G': [('F', 3)]
}


dist = {}
h = {
    'S': 13, 'A': 12, 'B': 4, 'C': 7, 'D': 3, 'E': 8, 'F': 2, 'H': 4, 'I': 9, 'G': 0
}


def bestFit(start, target):
    q = []
    q.append((h[start], start))
    for x in graph:
        dist[x] = 10000
    dist[start] = 0

    while q:
        print()
        q = sorted(q)
        curr = q.pop(0)
        print(curr)
        curr_dist = dist[curr[1]]
        for node in graph[curr[1]]:
            if curr_dist+node[1] < dist[node[0]]:
                print(node, end=" ")
                dist[node[0]] = curr_dist + node[1]
                q.append((h[node[0]], node[0]))
    print(dist)


bestFit('S', 'G')
