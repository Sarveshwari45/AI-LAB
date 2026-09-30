environment = {
    "A": "Dirty",
    "B": "Dirty"
}

model = {
    "A": "Unknown",
    "B": "Unknown"
}

location = "A"


def vacuum_agent(location, environment, model):

    print("\nAgent is in room:", location)
    
    current_state = environment[location]

    model[location] = current_state

    if current_state == "Dirty":

        print("Room is Dirty")
        print("Action: SUCK")

        environment[location] = "Clean"

        model[location] = "Clean"

    else:

        print("Room is Clean")

        if location == "A":
            location = "B"
            print("Action: MOVE RIGHT")

        else:
            location = "A"
            print("Action: MOVE LEFT")

    return location


for i in range(5):

    location = vacuum_agent(
        location,
        environment,
        model
    )

    print("Environment:", environment)
    print("Agent Model:", model)


print("\nFinal Environment:", environment)
print("Final Model:", model)
