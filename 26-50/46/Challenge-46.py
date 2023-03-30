def fifth(*args):
    return type(args[4]) if len(args) >= 5 else "Not enough arguments"