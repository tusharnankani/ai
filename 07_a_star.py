graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('S', 1), ('C', 1), ('B', 2)],
    'B': [('A', 2), ('D', 5)],
    'C': [('A', 1), ('D', 3), ('G', 4)],
    'D': [('B', 5), ('C', 3), ('G', 2)],
    'G': [('D', 2), ('C', 4)]
}


dist = {}
h = {
    'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0
}


def Astar(start, target):
    q = []
    q.append((h[start], start))
    for x in graph:
        dist[x] = 10000
    dist[start] = 0

    while q:
        q = sorted(q)
        curr = q.pop(0)

        curr_dist = dist[curr[1]]
        for node in graph[curr[1]]:
            if curr_dist+node[1] < dist[node[0]]:
                dist[node[0]] = curr_dist + node[1]
                q.append((h[node[0]]+dist[node[0]], node[0]))

    print(dist)


Astar('S', 'G')
