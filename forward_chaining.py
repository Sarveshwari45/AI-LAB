
# Forward Chaining in First Order Logic

def forward_chaining(facts, rules, query):

    while True:
        new_facts = []

        for rule in rules:
            conditions, conclusion = rule.split("->")

            conditions = [x.strip() for x in conditions.split("&")]
            conclusion = conclusion.strip()

            # Check whether all conditions are satisfied
            if all(condition in facts for condition in conditions):

                if conclusion not in facts:
                    new_facts.append(conclusion)

        # Stop if no new facts are generated
        if not new_facts:
            break

        facts.extend(new_facts)

        print("\nNew Facts Generated:")
        for fact in new_facts:
            print(fact)

    # Check the query
    if query in facts:
        print("\nQuery Proved Successfully!")
    else:
        print("\nQuery Cannot Be Proved!")


# Main Program
print("FORWARD CHAINING IN FIRST ORDER LOGIC")

n = int(input("Enter number of facts: "))

facts = []
for i in range(n):
    facts.append(input("Enter fact: "))

r = int(input("Enter number of rules: "))

rules = []
for i in range(r):
    rules.append(input("Enter rule (use & and ->): "))

query = input("Enter query to prove: ")

forward_chaining(facts, rules, query)
