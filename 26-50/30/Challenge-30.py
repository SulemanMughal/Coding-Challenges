def format_date(date):
    m, d, y = date.split('/')
    return ''.join((y, d, m))