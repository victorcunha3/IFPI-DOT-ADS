'''8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo
ou negativo. A função deve retornar um valor booleano.'''

def valor_negativo(valor):
    if type(valor) == str:
        return Exception
    if valor < 0:
        return False
    else:
        return True

assert valor_negativo(2) == True
assert valor_negativo(4) ==True
assert valor_negativo(-43) ==False
assert valor_negativo('fsf') == Exception
assert valor_negativo(-48393) == False
assert valor_negativo(-48.393) == False
assert valor_negativo(4.57) ==True
print('ok')