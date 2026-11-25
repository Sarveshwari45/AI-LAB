
import math

def alpha_beta(node, depth, alpha, beta, maximizing_player, path="Root"):

    # Step 1: Check terminal condition
    if depth == 0 or isinstance(node, int):
        print(f"{path}: Leaf node value = {node}")
        return node

    # Step 2: MAX player's turn
    if maximizing_player:

        value = -math.inf

        print(f"\n{path}: MAX node")
        print(f"Initial Alpha = {alpha}, Beta = {beta}")

        for i, child in enumerate(node):

            print(f"\nExploring {path}.{i+1}")

            child_value = alpha_beta(
                child, depth - 1,
                alpha, beta, False,
                path + "." + str(i+1)
            )

            value = max(value, child_value)

            print(f"{path}: MAX({value}, {child_value}) = {value}")

            old_alpha = alpha
            alpha = max(alpha, value)

            print(f"Alpha updated: {old_alpha} -> {alpha}")

            # Beta pruning
            if alpha >= beta:
                print(f"PRUNING at {path}!")
                print(f"Alpha ({alpha}) >= Beta ({beta})")
                print("Remaining children are skipped.")
                break

        print(f"{path}: MAX returns {value}")
        return value

    # Step 3: MIN player's turn
    else:

        value = math.inf

        print(f"\n{path}: MIN node")
        print(f"Initial Alpha = {alpha}, Beta = {beta}")

        for i, child in enumerate(node):

            print(f"\nExploring {path}.{i+1}")

            child_value = alpha_beta(
                child, depth - 1,
                alpha, beta, True,
                path + "." + str(i+1)
            )

            value = min(value, child_value)

            print(f"{path}: MIN({value}, {child_value}) = {value}")

            old_beta = beta
            beta = min(beta, value)

            print(f"Beta updated: {old_beta} -> {beta}")

            # Alpha pruning
            if beta <= alpha:
                print(f"PRUNING at {path}!")
                print(f"Beta ({beta}) <= Alpha ({alpha})")
                print("Remaining children are skipped.")
                break

        print(f"{path}: MIN returns {value}")
        return value


# Main program

print("ALPHA-BETA PRUNING")

n = int(input("Enter number of child nodes of root: "))

tree = []

for i in range(n):
    m = int(input(f"Enter number of leaf nodes in child {i+1}: "))

    leaves = []

    for j in range(m):
        val = int(input(f"Enter value of leaf {i+1}.{j+1}: "))
        leaves.append(val)

    tree.append(leaves)

depth = 2

print("\nInitial Game Tree:", tree)
print("\nStarting Alpha-Beta Pruning...\n")

result = alpha_beta(
    tree, depth,
    -math.inf, math.inf,
    True
)

print("\n========== FINAL RESULT ==========")
print("Optimal value:", result)
