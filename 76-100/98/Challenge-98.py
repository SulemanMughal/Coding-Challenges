def next_letters(s):
    if not s:
        return 'A'
    elif s[-1] == 'Z':
        return next_letters(s[:-1]) + 'A'
    else:
        return s[:-1] + chr(ord(s[-1]) + 1)