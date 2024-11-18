def hill_climbing(func, start, step_size=0.1, iterations=100):
    current = start
    for _ in range(iterations):
        neighbors = [current - step_size, current + step_size]
        next_move = max(neighbors, key=func)  # Choose the neighbor with the highest function value
        
        if func(next_move) <= func(current):  # If no better move, stop
            break
        current = next_move
    return current

# Example usage
def objective_function(x):
    return -(x - 3)**2 + 10  # Parabola with a maximum at x = 3

start = 0  # Initial starting point
optimal_x = hill_climbing(objective_function, start)
print(f"Optimal x: {optimal_x}")
print(f"Maximum value of the function: {objective_function(optimal_x)}")
