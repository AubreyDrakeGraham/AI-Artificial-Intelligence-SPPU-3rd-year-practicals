colors=["Red","Blue"]
states=["A","B","C","D"]
neighbours={"A":["B","C"],"B":["A","D"],"C":["A","D"],"D":["B","C"]}
color_of_states={}
def promising(state,color):
    for neighbour in neighbours.get(state):
        color_of_neighbour = color_of_states.get(neighbour)
        if color_of_neighbour == color:
            return False
        else:
            return True

def get_color_of_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        color_of_states[state] = get_color_of_state(state)
    print(color_of_states)

main()
