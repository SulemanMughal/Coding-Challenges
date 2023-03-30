def num_to_eng(n):
    if n == 0:
        return 'zero'
    
    unit = ('','one','two','three','four','five','six','seven','eight','nine')
    tens = ('','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')
    teen = ('ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
    h, t, u = '', '', ''
    
    if n//100:
        h = unit[n//100] + ' hundred'
        n = n%100
    
    if n >= 20:
        t = tens[n//10]
        n = n%10
    elif n >= 10:
        t = teen[n-10]
        n = 0
    
    u = unit[n]
    
    return ' '.join(filter(None,[h,t,u]))