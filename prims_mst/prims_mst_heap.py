import heapq

def read_graph(file_path):
    """Reads the graph from the given file and returns the graph as an adjacency list."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    num_nodes, num_edges = map(int, lines[0].split())
    graph = {i: [] for i in range(1, num_nodes + 1)}

    for line in lines[1:]:
        u, v, cost = map(int, line.split())
        graph[u].append((cost, v))
        graph[v].append((cost, u))

    return graph

def prim_mst(graph):
    """Calculates the total cost of the MST using Prim's algorithm."""
    start_node = next(iter(graph))  # Start from any node (e.g., the first one)
    visited = set()
    min_heap = []
    total_cost = 0

    # Add all edges from the start node to the heap
    visited.add(start_node)
    for cost, neighbor in graph[start_node]:
        heapq.heappush(min_heap, (cost, neighbor))

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            # Include this node in the MST
            visited.add(node)
            total_cost += cost

            # Add all edges from this node to the heap
            for edge_cost, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_cost, neighbor))

    return total_cost

if __name__ == "__main__":
    file_path = "edges.txt"  # Replace with the path to your graph file
    graph = read_graph(file_path)
    mst_cost = prim_mst(graph)
    print(f"Total cost of the minimum spanning tree: {mst_cost}")