import math
import random

def objective_function(x):
    """The function we want to maximize."""
    return x * math.sin(x)

def hill_climb(start_x, step_size, max_iterations):
    """
    Perform the hill climbing algorithm to find the maximum value of the objective function.

    Parameters:
    start_x (float): The starting point for x.
    step_size (float): The amount by which x is incremented or decremented.
    max_iterations (int): The maximum number of iterations allowed.

    Returns:
    (float, float): The x-value and objective function value at the maximum point found.
    """
    current_x = start_x
    current_value = objective_function(current_x)

    for iteration in range(max_iterations):
        # Generate possible new points by moving up and down by the step size
        neighbors = [current_x + step_size, current_x - step_size]

        # Evaluate the function at the neighboring points
        neighbor_values = [objective_function(neighbor) for neighbor in neighbors]

        # Find the best neighbor
        max_neighbor_value = max(neighbor_values)
        best_neighbor = neighbors[neighbor_values.index(max_neighbor_value)]

        # If the best neighbor is better than the current, move to that neighbor
        if max_neighbor_value > current_value:
            current_x = best_neighbor
            current_value = max_neighbor_value
            print(f"Iteration {iteration + 1}: x = {current_x:.4f}, f(x) = {current_value:.4f}")
        else:
            # If no improvement, stop the algorithm (we've reached a peak)
            print("Reached a peak.")
            break

    return current_x, current_value

# Define parameters for the hill climbing algorithm
start_x = random.uniform(0, 10)  # Start at a random point within the range [0, 10]
step_size = 0.1                  # Step size to adjust x
max_iterations = 100             # Maximum number of iterations

# Run hill climbing to maximize the function
best_x, best_value = hill_climb(start_x, step_size, max_iterations)

print(f"\nOptimal x: {best_x:.4f}")
print(f"Maximum value of f(x): {best_value:.4f}")
