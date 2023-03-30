# Non-Recursive Solution

import re

    
def find_longest(s):
        return max(re.split('\W', s.lower()), key=len)


# Recursive Solution

def find_longest(s, recur=0):
    if recur == 0:
        s = "".join(w for w in s.replace("'s","") if w.isalpha() or w==" ")
    s = s.split()
    s.pop(-(len(s[-2]) < len(s[-1]))-1)
    return s[0].lower() if len(s)==1 else find_longest(" ".join(s),1)