def look_and_say(n):
    n = str(n)
    if len(n)%2:
        return 'invalid'
    return int(''.join(int(n[i]) * n[i+1] for i in range(0, len(n), 2)))