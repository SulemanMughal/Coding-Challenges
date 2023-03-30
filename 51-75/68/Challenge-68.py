def create_square(n):
    if not n or n < 1:
        return ''
    elif n == 1:
        return '#'
    else:
        top = ['#'*n]
        bot = ['#'*n]
        mid = ['#' + ' '*(n-2) + '#'] * (n-2)
        return '\n'.join(top+mid+bot)