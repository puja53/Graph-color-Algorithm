
# PUJA BARMAN
# ID 212902053
# List of available colors
colors = [ 'Green','Red', 'Blue', 'Orange', 'Yellow']


# Function to check if a color can be assigned to a state based on its neighbors' colors
def find_color(state, color, neighbors, states_color):
    for neighbor in neighbors.get(state, []):
        neighbor_color = states_color.get(neighbor)
        if neighbor_color == color:
            return False
    return True


# Function to get the color to be assigned to a state
def get_color(state, colors, neighbors, states_color):
    for color in colors:
        if find_color(state, color, neighbors, states_color):
            return color
    return None


# Main function to assign colors to states
def main():
    # Input number of states
    num_states = int(input("Enter the number of states: "))

    # Input state names
    states = []
    for i in range(num_states):
        state_name = input(f"Enter the name of state {i + 1}: ")
        states.append(state_name)

    # Input neighbors of each state
    neighbors = {}
    for state in states:
        neighbors[state] = input(f"Enter neighbors of {state}: ").split()

    # Dictionary to store the color assigned to each state
    states_color = {}

    # Iterate through each state
    for state in states:
        # Get the color for the current state
        states_color[state] = get_color(state, colors, neighbors, states_color)

    # Print coloring result
    for state, color in states_color.items():
        print(f"{state}: {color}")


if __name__ == "__main__":
    main()
