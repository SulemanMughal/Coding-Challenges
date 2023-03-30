def mark_maths(lst):
    lst=[eval(i.replace('=','==')) for i in lst]
    return str(round(100*sum(lst)/len(lst)))+'%'