def expensive_orders(d, p):
    return {k: v for k, v in d.items() if v > p}