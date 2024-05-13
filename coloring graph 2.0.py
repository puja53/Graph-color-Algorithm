# List of available colors
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']

# List of states
states = ['Bangladesh', 'India', 'Japan', 'Germanny']

# Dictionary representing neighbors of each state
neighbors = {
    'Bangladesh': ['India', 'Japan'],
    'India': ['Bangladesh', 'Japan', 'Germanny'],
    'Japan': ['Bangladesh', 'India', 'Germanny'],
    'Germanny': ['India', 'Japan']
}

# Dictionary to store the color assigned to each state
states_color = {}

# Function to check if a color can be assigned to a state based on its neighbors' colors
def find_color(state, color):
    for i in neighbors.get(state):
        neighbor_color = states_color.get(i)
        if neighbor_color == color:
            return False
    return True

# Function to get the color to be assigned to a state
def get_color(state):
    for j in colors:
        if find_color(state, j):
            return j

# Main function to assign colors to states
def main():
    # Iterate through each state
    for state in states:
        # Get the color for the current state
        states_color[state] = get_color(state)


    for state, color in states_color.items():
        print(f"{state}: -------->>{color}")


main()