score = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5}
def check_score(s):
    return max(0, sum(score[val] for row in s for val in row))