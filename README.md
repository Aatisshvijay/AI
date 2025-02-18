# AI

vaccum cleaner
class SimpleReflexAgent:
    def __init__(self):  # Corrected constructor
        self.current_room = 0  # Start at room A

    def perceive(self, room_states):
        # Perceive the state of the current room
        return room_states[self.current_room]

    def act(self, perception, room_states):
        # Act based on the perception
        if perception == 'dirty':
            print(f"Room {chr(self.current_room + ord('A'))} is dirty. Cleaning...")
            room_states[self.current_room] = 'clean'
        else:
            print(f"Room {chr(self.current_room + ord('A'))} is already clean.")

        # Move to the next room if there are more rooms left
        if self.current_room < len(room_states) - 1:
            self.current_room += 1
            print(f"Moving to Room {chr(self.current_room + ord('A'))}")
        else:
            print("All rooms have been checked.")

# Initialize the simple reflex agent
simple_agent = SimpleReflexAgent()

# Initial states of rooms: all dirty
room_states = ['dirty', 'dirty', 'dirty', 'dirty']
while 'dirty' in room_states:
    current_perception = simple_agent.perceive(room_states)
    simple_agent.act(current_perception, room_states)

print("Final Room States:", room_states)
