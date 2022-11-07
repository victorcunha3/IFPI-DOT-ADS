def numero_primo(n):
    if type(n) != int:
        return Exception

    if n == 1:
        return False

    e_primo = True
    for i in range(2,n):
        if n % i == 0:
            e_primo = False
    return e_primo



assert numero_primo(3) == True
assert numero_primo(1) == False
assert numero_primo(88) == False
assert numero_primo(7) == True
assert numero_primo(9) == False
assert numero_primo(13) == True
assert numero_primo(6.9) == Exception
assert numero_primo('gjsjsgus') == Exception
assert numero_primo(77) == False

print('todos ok')