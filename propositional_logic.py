from itertools import product

# Define implication function
def implies(p, q):
    return not p or q


# Define Knowledge Base
# Q → P
# P → ¬Q
# Q ∨ R

def KB(P, Q, R):
    return (implies(Q, P) and
            implies(P, not Q) and
            (Q or R))


# Define Query
# Query: R

def query(P, Q, R):
    return R


# Generate all possible truth assignments
symbols = ['P', 'Q', 'R']

print("\nTRUTH TABLE ENUMERATION")
print("-" * 65)

print(f"{'P':^8}{'Q':^8}{'R':^8}"
      f"{'Q->P':^8}{'P->~Q':^8}"
      f"{'Q|R':^8}{'KB':^8}{'Query':^8}")

print("-" * 65)

entails = True

# Generate 2^3 = 8 models
for values in product([True, False], repeat=3):

    P, Q, R = values

    a = implies(Q, P)
    b = implies(P, not Q)
    c = Q or R

    kb = KB(P, Q, R)
    alpha = query(P, Q, R)

    # Check entailment
    if kb and not alpha:
        entails = False

    print(f"{str(P):^8}{str(Q):^8}{str(R):^8}"
          f"{str(a):^8}{str(b):^8}"
          f"{str(c):^8}{str(kb):^8}"
          f"{str(alpha):^8}")

print("-" * 65)

# Display final result
if entails:
    print("\nKB entails Query R")
    print("ENTAILMENT: TRUE")
else:
    print("\nKB does not entail Query R")
    print("ENTAILMENT: FALSE")
