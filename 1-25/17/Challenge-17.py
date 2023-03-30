def calculator(n1, operator, n2):
    try: 
        return eval(str(n1)+operator+str(n2))
    except ZeroDivisionError:
        return "Can't divide by 0!"