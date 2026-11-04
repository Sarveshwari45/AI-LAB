import math
import random

# Objective function
def objective(x):
    return x**2 + 10 * math.sin(x)

# Taking input from user
current = float(input("Enter initial solution: "))
temperature = float(input("Enter initial temperature: "))
cooling_rate = float(input("Enter cooling rate (e.g. 0.95): "))
min_temp = float(input("Enter minimum temperature: "))

current_cost = objective(current)

best = current
best_cost = current_cost

# Simulated Annealing
while temperature > min_temp:

    # Generate neighboring solution
    new = current + random.uniform(-1, 1)
    new_cost = objective(new)

    delta = new_cost - current_cost

    # Acceptance condition
    if delta < 0 or random.random() < math.exp(-delta / temperature):
        current = new
        current_cost = new_cost

    # Update best solution
    if current_cost < best_cost:
        best = current
        best_cost = current_cost

    # Decrease temperature
    temperature *= cooling_rate

# Display result
print("\nBest Solution:", best)
print("Minimum Cost:", best_cost)
