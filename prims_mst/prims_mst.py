# Open the file in read mode
with open('edges.txt', 'r') as file:
    # Read each line in the file
    lines = file.readlines()
    n, m = map(int, lines[0].split())
    edges = []
    for line in lines[1:]:
        u, v, cost = map(int, line.split())
        edges.append((u, v, cost))

    # find the minumum spanning tree with prims algorithm without heap
    visited = set()
    total_cost = 0
    visited.add(1)
    while len(visited) < n:
        min_cost = float('inf')
        min_edge = None
        for u, v, cost in edges:
            if u in visited and v not in visited and cost < min_cost:
                min_cost = cost
                min_edge = (u, v)
            elif v in visited and u not in visited and cost < min_cost:
                min_cost = cost
                min_edge = (v, u)
        visited.add(min_edge[1])
        total_cost += min_cost
    print(visited)
    print(total_cost)