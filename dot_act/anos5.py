'''Faça uma função que recebe a idade de uma pessoa em anos, meses e dias
e retorna essa idade expressa em dias.'''


def idade_person(anos,meses,dias):
    if type(anos) != int or type(meses) != int or type(dias) != int:
        return Exception
    if (anos not in range(0,121)) or (meses not in range(0,13)) or (dias not in range(0,31)):
        return Exception
    return anos*365 + meses*30 + dias


assert idade_person(10,2,2) == 3712
assert idade_person(17,2,9) == 6274
assert idade_person('17',2,9) == Exception
assert idade_person('17','17',9) == Exception

print('ok')
