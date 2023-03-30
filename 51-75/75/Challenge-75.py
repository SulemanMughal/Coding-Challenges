def can_see_stage(seats):
    return all(sorted(set(row)) == list(row) for row in zip(*seats))