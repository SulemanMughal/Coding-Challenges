def get_frame(w, h, ch):
    if w <= 2 or h <= 2:
        return 'invalid'
    head = ch*w
    side = ch + ' '*(w-2) + ch
    return [[i] for i in [head] + [side]*(h-2) + [head]]