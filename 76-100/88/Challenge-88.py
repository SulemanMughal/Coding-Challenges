def letter_combinations(digits):
    dic = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
    ans = ['']
    for d in digits:
        ans = [a+e for a in ans for e in dic[int(d)]]
    return ans