class VacuumCleaner:
    def __init__(self, location, room_A, room_B):
        self.location = location
        self.rooms = {
            "A": room_A,
            "B": room_B
        }

    def display(self):
     
        print("Room A:", self.rooms["A"])
        print("Room B:", self.rooms["B"])
        print("Vacuum Location:", self.location)
       

    def suck(self):
        print("Action: SUCK")
        self.rooms[self.location] = "Clean"
 
    def move_left(self):
        print("Action: MOVE LEFT")
        self.location = "A"

    def move_right(self):
        print("Action: MOVE RIGHT")
        self.location = "B"

    def goal_test(self):
        return self.rooms["A"] == "Clean" and self.rooms["B"] == "Clean"

    def agent(self):
       
        if self.rooms[self.location] == "Dirty":
            self.suck()

        elif self.location == "A":
            self.move_right()

        elif self.location == "B":
            self.move_left()



print("VACUUM CLEANER AGENT")

location = input("Enter vacuum cleaner location (A/B): ").upper()

while location not in ["A", "B"]:
    location = input("Please enter A or B: ").upper()

room_A = input("Is Room A dirty? (yes/no): ").lower()

while room_A not in ["yes", "no"]:
    room_A = input("Please enter yes or no: ").lower()

room_B = input("Is Room B dirty? (yes/no): ").lower()

while room_B not in ["yes", "no"]:
    room_B = input("Please enter yes or no: ").lower()


room_A = "Dirty" if room_A == "yes" else "Clean"
room_B = "Dirty" if room_B == "yes" else "Clean"


vacuum = VacuumCleaner(location, room_A, room_B)

print("\nInitial State:")
vacuum.display()


while not vacuum.goal_test():
    vacuum.agent()
    vacuum.display()

print("\nGoal achieved!")
print("Both Room A and Room B are clean.")
