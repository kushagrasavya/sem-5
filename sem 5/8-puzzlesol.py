from heapq import heappop, heappush

def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):  # Numbers 1 to 8
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)  # Find the blank space (0)
    x, y = divmod(zero_idx, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            swap_idx = nx * 3 + ny
            new_state = list(state)
            new_state[zero_idx], new_state[swap_idx] = new_state[swap_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))

    return neighbors

def a_star_8_puzzle(start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]

        for neighbor in get_neighbors(current):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor, goal)
                heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current

    return None

# Example usage
start_state = (1, 2, 3, 4, 0, 5, 6, 7, 8)  # Initial state
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)   # Goal state

solution = a_star_8_puzzle(start_state, goal_state)
if solution:
    print("Solution steps:")
    for step in solution:
        print(step[:3], "\n", step[3:6], "\n", step[6:], "\n")
else:
    print("No solution found.")
