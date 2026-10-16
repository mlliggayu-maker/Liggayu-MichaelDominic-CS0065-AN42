#Task 1
#initializing two rooms using python dictionary

rooms = {
    "Room A": input("Is Room A Dirty or clean?: "),
    "Room B": input("Is Room B Dirty or clean?: ")
}

#creating function to check if the room is dirty.
def is_dirty(room):
    return rooms[room] == "dirty"

#creating a function to clean a room.
def clean_room(room):
    rooms[room] = "clean"
#Task 2
#creating class for agent
class Agents:
    #set the agent's starting location
    def __init__(self, location):
        self.location = location

    #decide what action to take based on the room's state using perceive and act method
    def perceive_and_act(self):

        #Rule 1: If the current room is dirty clean it.
        if is_dirty(self.location):
            clean_room(self.location)
            return "Cleaned"
        #Rule 2: If the current room is clean, move to the other room
        else:
            self.move()
            return "Moved"
    #implement move method to move agent to the other room
    def move(self):
        if self.location == "Room A":
            self.location = "Room B"
        else:
            self.location = "Room A"

#Task 3
 #Asking the user where the agent start.
start = input("Enter the starting room (A/B): ").upper()
if start == "A":
    start = "Room A"
else:
    start = "Room B"

#create the agent
agent = Agents (start)
steps = int(input("Enter number of steps: "))

#Run the agent for specified number of steps.
for step in range (1, steps +1):

 #let the agent perceive the room and perform an action.
    action = agent.perceive_and_act()

    #displaying results

    print("\nStep", step)
    print ("Location:", agent.location)
    print ("Action:", action)
    print ("Rooms:", rooms)
