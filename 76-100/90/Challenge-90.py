from fractions import Fraction
def farey(n):
    r=range(1,n+1)
    a=sorted(set(Fraction(i,j) for i in r for j in r if i<j))
    return ['0/1']+list(map(str,a))+['1/1']