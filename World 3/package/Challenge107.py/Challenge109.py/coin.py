def coin(n = 0, coin = '€'):
    return f'{coin}{n:.2f}'.replace('.',',')


def increase(n = 0, i = 0, formato=False):
    result = n + (n * i / 100)
    return result if formato is False else coin(result)
   

def decrease(n = 0, d = 0, formato=False):
    result = n - (n * d / 100)
    return result if formato is False else coin(result)
    


def double(n = 0, formato=False):
    result = n * 2
    return result if formato is False else coin(result)
 

def half(n = 0, formato=False):
    result = n / 2
    return result if format is False else coin(result)
