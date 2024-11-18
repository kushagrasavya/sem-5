import random

# Objective function (to maximize)
def objective_function(x):
    return -(x - 3)**2 + 10  # Parabola with a maximum at x = 3

# Create an initial population of random solutions
def create_population(pop_size, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(pop_size)]

# Select two parents based on their fitness (tournament selection)
def select_parents(population, fitness_scores):
    parents = random.choices(population, weights=fitness_scores, k=2)
    return parents

# Crossover operation (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.uniform(0, 1)
    child1 = crossover_point * parent1 + (1 - crossover_point) * parent2
    child2 = crossover_point * parent2 + (1 - crossover_point) * parent1
    return child1, child2

# Mutation operation (random mutation)
def mutate(child, mutation_rate, lower_bound, upper_bound):
    if random.random() < mutation_rate:
        child += random.uniform(-1, 1)  # Small random change
        child = max(lower_bound, min(child, upper_bound))  # Ensure within bounds
    return child

# Genetic Algorithm function
def genetic_algorithm(pop_size, lower_bound, upper_bound, generations, mutation_rate):
    population = create_population(pop_size, lower_bound, upper_bound)
    
    for generation in range(generations):
        # Calculate fitness scores for each individual
        fitness_scores = [objective_function(individual) for individual in population]
        
        # Print the best individual of this generation
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        print(f"Generation {generation}: Best = {best_individual}, Fitness = {max(fitness_scores)}")
        
        # Create a new population through selection, crossover, and mutation
        new_population = []
        for _ in range(pop_size // 2):  # Select pairs of parents
            parent1, parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate, lower_bound, upper_bound))
            new_population.append(mutate(child2, mutation_rate, lower_bound, upper_bound))
        
        population = new_population  # Replace the old population with the new one
    
    # Return the best individual found
    fitness_scores = [objective_function(individual) for individual in population]
    best_individual = population[fitness_scores.index(max(fitness_scores))]
    return best_individual

# Example usage
pop_size = 10  # Population size
lower_bound = 0  # Lower bound of the search space
upper_bound = 6  # Upper bound of the search space
generations = 50  # Number of generations
mutation_rate = 0.1  # Mutation rate

best_solution = genetic_algorithm(pop_size, lower_bound, upper_bound, generations, mutation_rate)
print(f"Best solution found: x = {best_solution}")
print(f"Fitness value: {objective_function(best_solution)}")
