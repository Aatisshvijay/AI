class TableDrivenAgent:
    def __init__(self):
        # Rules for cleaning rooms based on their states
        self.table = {
            ('dirty', 'dirty', 'dirty', 'dirty'): ['clean A'],
            ('clean', 'dirty', 'dirty', 'dirty'): ['clean B'],
            ('clean', 'clean', 'dirty', 'dirty'): ['clean C'],
            ('clean', 'clean', 'clean', 'dirty'): ['clean D'],
            ('clean', 'clean', 'clean', 'clean'): ['all clean'],
        }

    def perceive(self, room_states):
        # Return the current state as a tuple
        return tuple(room_states)

    def act(self, current_state):
        # Retrieve actions from the table based on the current state
        return self.table.get(current_state, ['Invalid State'])


# Initialize the table-driven agent
table_agent = TableDrivenAgent()

# Initial states of rooms: all dirty
room_states = ['dirty', 'dirty', 'dirty', 'dirty']
while 'dirty' in room_states:
    current_state = table_agent.perceive(room_states)
    actions = table_agent.act(current_state)
    for action in actions:
        if action == 'all clean':
            print("All rooms are clean!")
            break
        elif action.startswith('clean'):
            # Clean the room specified in the action
            room = action.split()[-1]
            room_index = ord(room) - ord('A')
            print(f"Action: Cleaning Room {room}")
            room_states[room_index] = 'clean'
        else:
            print(f"Action: {action}")  # For invalid states or moves

print("Final Room States:", room_states)
