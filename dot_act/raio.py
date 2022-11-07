'''1. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o
seu volume (v = 4/3 * PI * R**3).'''

def calcular_raio(raio):
    if type(raio) == str or raio < 0:
        return Exception
    return round(4/3 * 3.14 * raio**3,2)



assert calcular_raio(0) == 0
assert calcular_raio(-367) == Exception
assert calcular_raio('fgdf') == Exception
assert calcular_raio(1) == 4.19
assert calcular_raio(1.00) == 4.19

print('okay')