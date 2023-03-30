def longest_substring(digits):
    res = digits[0]
    for i in digits[1:]:
        if int(i)%2 != int(res[-1])%2:
            res += i
        else:
            res += ' ' + i
    return max(res.split(), key=len)