from re import search, IGNORECASE
def find_pattern(dict_, p):
    return sorted("{} = {}".format(k, p if search(p, v, IGNORECASE) else None)
            for k, v in dict_.items())