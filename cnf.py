
import re

# Step 1: Eliminate biconditional and implication
def eliminate_implication(expr):
    expr = re.sub(
        r'(\w+)\s*<->\s*(\w+)',
        r'((NOT \1 OR \2) AND (NOT \2 OR \1))',
        expr
    )

    expr = re.sub(
        r'(\w+)\s*->\s*(\w+)',
        r'(NOT \1 OR \2)',
        expr
    )

    return expr


# Step 2: Move negation inward
def move_negation(expr):
    expr = expr.replace(
        "NOT (NOT ", ""
    )
    expr = expr.replace("))", ")")

    expr = expr.replace(
        "NOT (", "NOT("
    )

    return expr


# Step 3: Standardize variables
def standardize_variables(expr):
    variables = re.findall(
        r'(FORALL|EXISTS)\s+(\w+)', expr
    )

    for i, (quantifier, var) in enumerate(variables):
        new_var = var + str(i + 1)
        expr = re.sub(
            rf'\b{var}\b', new_var, expr
        )

    return expr


# Step 4: Skolemization
def skolemization(expr):
    count = 0

    def replace_existential(match):
        nonlocal count
        count += 1
        return "Sk" + str(count)

    expr = re.sub(
        r'EXISTS\s+\w+',
        replace_existential,
        expr
    )

    return expr


# Step 5: Remove universal quantifiers
def remove_universal(expr):
    expr = re.sub(
        r'FORALL\s+\w+\s*', '', expr
    )
    return expr


# Step 6: Distribute OR over AND
def distribute_or(expr):
    expr = expr.replace(
        "OR (", "OR("
    )

    # Basic distribution for simple expressions
    pattern = r'(\w+)\s+OR\s+\((\w+)\s+AND\s+(\w+)\)'

    while re.search(pattern, expr):
        expr = re.sub(
            pattern,
            r'((\1 OR \2) AND (\1 OR \3))',
            expr
        )

    return expr


# Main program
print("FOL TO CNF CONVERSION")

formula = input("Enter FOL expression: ")

print("\nOriginal Formula:", formula)

formula = eliminate_implication(formula)
print("\nAfter eliminating implication:", formula)

formula = move_negation(formula)
print("\nAfter moving negation:", formula)

formula = standardize_variables(formula)
print("\nAfter standardizing variables:", formula)

formula = skolemization(formula)
print("\nAfter Skolemization:", formula)

formula = remove_universal(formula)
print("\nAfter removing universal quantifiers:", formula)

formula = distribute_or(formula)
print("\nFinal CNF:", formula)
