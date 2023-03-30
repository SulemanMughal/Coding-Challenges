def censor(s):
    return ' '.join('*'*len(i) if len(i) > 4 else i for i in s.split())