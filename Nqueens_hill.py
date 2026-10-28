import random


def calculate_cost(state):
    n = len(state)
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def display_board(state):
    n = len(state)

    for row in range(n):
        print(" ".join(
            "Q" if state[col] == row else "."
            for col in range(n)
        ))


def get_neighbors(state):
    n = len(state)
    neighbors = []

    for i in range(n):
        for j in range(i + 1, n):
            new_state = state.copy()
            new_state[i], new_state[j] = (
                new_state[j], new_state[i]
            )

            neighbors.append((new_state, (i, j),
                              calculate_cost(new_state)))

    return neighbors


def hill_climbing(n):
    if n in (2, 3):
        print("No solution exists for N =", n)
        return

    step = 0

    while True:
        current = list(range(n))
        random.shuffle(current)

        while True:
            current_cost = calculate_cost(current)

            print(f"\nStep {step}")
            print("Current State:")
            display_board(current)
            print("Cost:", current_cost)

            if current_cost == 0:
                print("\nFINAL SOLUTION:")
                display_board(current)
                print("Final Cost: 0")
                print("Total Moves:", step)
                return

            neighbors = get_neighbors(current)
            best_state, best_pair, best_cost = min(
                neighbors,
                key=lambda x: (x[2], x[1])
            )

            if best_cost >= current_cost:
                print("Local minimum reached. Restarting...")
                break

            current = best_state
            step += 1

            print("Selected Swap:", best_pair)
            print("Next State:")
            display_board(current)
            print("New Cost:", best_cost)


n = int(input("Enter the value of N: "))

if n < 1:
    print("N must be positive.")
else:
    hill_climbing(n)


