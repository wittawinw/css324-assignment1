def initial_state():
    return (8, 0, 0)

def is_goal(s):
    a, b, _ = s
    return a == 4 and b == 4

def successors(s):
    a, b, c = s
    max_capacity = [8, 5, 3]

    
    successor_states = []

    for source in range(3):
        for target in range(3):
            if source != target:
                
                amount_to_pour = min(a, max_capacity[target] - b)

                
                if amount_to_pour > 0:
                    new_state = list(s)
                    new_state[source] -= amount_to_pour
                    new_state[target] += amount_to_pour
                    successor_states.append(((new_state[0], new_state[1], new_state[2]), amount_to_pour))

    return successor_states
