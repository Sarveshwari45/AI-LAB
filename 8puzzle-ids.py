def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),   
        (1, 0),    
        (0, -1),   
        (0, 1)     
    ]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = list(state)

            new_zero = nr * 3 + nc

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def depth_limited_search(state, goal, limit, path, visited):

    if state == goal:
        return path

    if limit == 0:
        return None

    visited.add(state)

    for neighbor in get_neighbors(state):

        if neighbor not in visited:

            result = depth_limited_search(
                neighbor,
                goal,
                limit - 1,
                path + [neighbor],
                visited
            )

            if result is not None:
                return result

    return None


def iterative_deepening(start, goal):

    depth = 0
    max_depth = 30

    while depth <= max_depth:

        visited = set()

        result = depth_limited_search(
            start,
            goal,
            depth,
            [start],
            visited
        )

        if result is not None:
            return result

        depth += 1

    return None


def print_state(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()



start = (
    1, 2, 3,
    0, 4, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


solution = iterative_deepening(start, goal)


if solution is not None:

    print("Goal state found!\n")

    print("Solution path:\n")

    for state in solution:
        print_state(state)

    print("Goal reached successfully!")

else:

    print("Goal state not found!")
