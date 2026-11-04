def unify(x, y, subs):

    if x == y:
        return True

    if x.islower() and len(x) == 1:
        subs[x] = y
        return True

    if y.islower() and len(y) == 1:
        subs[y] = x
        return True

    return False


def unification(e1, e2):

    subs = {}

    p1 = e1[:e1.index('(')]
    p2 = e2[:e2.index('(')]

    if p1 != p2:
        return None

    a = e1[e1.index('(')+1:-1].split(',')
    b = e2[e2.index('(')+1:-1].split(',')

    if len(a) != len(b):
        return None

    for x, y in zip(a, b):
        x = x.strip()
        y = y.strip()

        for key, value in subs.items():
            if x == key:
                x = value
            if y == key:
                y = value

        if not unify(x, y, subs):
            return None

    return subs


# Main program
print("UNIFICATION IN FIRST ORDER LOGIC")

e1 = input("Enter first expression: ")
e2 = input("Enter second expression: ")

result = unification(e1, e2)

if result is None:
    print("Unification Failed")
else:
    print("Unification Successful")
    print("Substitution:", result)
