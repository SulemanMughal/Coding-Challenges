def prime_factors(num):
    output = []
    for i in range(2,  int(num/2)):
        while num % i == 0:
            output.append(i)
            num = int(num / i)
    
    return output