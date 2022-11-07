
def perfeito(n):
    if type(n) != int:
        return Exception
        
    soma=0
    for x in range(1,n):
        if n % x == 0:
            soma = soma + x

    if soma==n:
        return True
    else:
        return False

assert perfeito(6) == True
assert perfeito(7) == False
assert perfeito(123) == False
assert perfeito('353') == Exception

print('ok')