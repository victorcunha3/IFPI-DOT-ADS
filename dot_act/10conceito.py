'''10. Faça uma função que recebe a média final de um aluno por parâmetro e
retorna o seu conceito, conforme a tabela abaixo:
Nota Conceito
de 0,0 a 4,9 D
de 5,0 a 6,9 C
de 7,0 a 8,9 B
de 9,0 a 10,0A'''


def conceito_nota(nota):
    if type(nota) == str:
        return Exception

    if nota >=0.0 and nota <=4.9:
        return 'D'
    elif nota >= 5.0 and nota <=6.9:
        return 'C'
    
    elif nota >= 7.0 and nota <=8.9:
        return 'B'

    elif nota >= 9.0 and nota <=10.0:
        return 'A'

    else:
        return False

assert conceito_nota(9.0) == 'A'
assert conceito_nota(4.7) == 'D'
assert conceito_nota(7.5) == 'B'
assert conceito_nota('SBCUDSYD') == Exception
assert conceito_nota(2.8) == 'D'
assert conceito_nota(2) == 'D'
assert conceito_nota(11) == False
assert conceito_nota(-11) == False

print('ok')