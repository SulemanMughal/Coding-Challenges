from datetime import datetime as dt
    
def sort_dates(lst, mode):
    lst.sort(key=lambda x: dt.strptime(x, '%d-%m-%Y_%H:%M'))
    return lst if mode == 'ASC' else lst[::-1]