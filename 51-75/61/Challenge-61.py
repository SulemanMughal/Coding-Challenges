def pop(state):
    ground = list(range(max(state) + 1))
    return ground + ground[::-1][1:]