

def par_impar(valor):
    if type(valor) != int:
        return Exception

    if valor % 2 == 0:
        return True

    elif valor % 2 != 0:
        return False

assert par_impar(6) == True
assert par_impar(3) == False
assert par_impar(483384) == True
assert par_impar(9) == False
assert par_impar(2.44) == Exception
print('ok')