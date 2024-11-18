from heapq import heappop, heappush

def a_star(graph, start, goal, heuristic):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        _, current = heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]

        for neighbor, cost in graph[current].items():
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current

    return None

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

heuristic = lambda x: {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0, 'F': 3}[x]  # Example heuristic
print(a_star(graph, 'A', 'F', heuristic))  # Expected Output: ['A', 'C', 'F']
