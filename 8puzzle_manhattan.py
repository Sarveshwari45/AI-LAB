
import heapq

# Initial state: exactly 4 moves from the goal
start = (1, 2, 3,
         8, 6, 4,
         0, 7, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)


# Manhattan distance heuristic
def h(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        row, col = divmod(i, 3)
        goal_pos = goal.index(tile)
        goal_row, goal_col = divmod(goal_pos, 3)

        distance += (
            abs(row - goal_row)
            + abs(col - goal_col)
        )

    return distance


# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    for dr, dc in [(-1, 0), (1, 0),
                   (0, -1), (0, 1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new_state = list(state)

            new_state[blank], new_state[pos] = (
                new_state[pos], new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* search
def astar(start, goal):
    open_list = [(h(start), 0, start)]
    parent = {start: None}
    g_cost = {start: 0}
    closed = set()

    while open_list:
        f, g, state = heapq.heappop(open_list)

        if state in closed:
            continue

        if state == goal:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        closed.add(state)

        for neighbor in get_neighbors(state):
            new_g = g + 1

            if new_g < g_cost.get(neighbor, float("inf")):
                g_cost[neighbor] = new_g
                parent[neighbor] = state

                new_f = new_g + h(neighbor)

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor)
                )

    return None


# Display puzzle
def display_state(state):
    for i in range(0, 9, 3):
        print(" ".join(
            "_" if x == 0 else str(x)
            for x in state[i:i+3]
        ))


# Execute
path = astar(start, goal)

if path:
    print("INITIAL STATE:")
    display_state(start)

    print("\nFINAL STATE:")
    display_state(goal)

    print("\nSOLUTION STEPS:")

    for step, state in enumerate(path):
        g = step
        hv = h(state)
        f = g + hv

        print(f"\nStep {step}:")
        print(f"g(n) = {g}")
        print(f"h(n) = {hv}")
        print(f"f(n) = {f}")
        display_state(state)

    print("\nTotal moves:", len(path) - 1)
else:
    print("No solution found")
