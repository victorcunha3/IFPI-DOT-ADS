'''2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma
letra. Se a letra for A o procedimento calcula a média aritmética das notas do
aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar
a média calculada.'''


def notas_aluno(n1,n2,n3,letra):
    if type(letra) != str or type(n1) == str or type(n2) == str or type(n3) == str :
        return Exception

    if letra == 'a':
        notas = (n1 + n2 + n3) / 3
        return round(notas,2)

    elif letra == 'p':
        notasP = ((n1*5) + (n2*3) + (n3*2) ) / 3
        return round(notasP,2)

    else:
        return False

assert notas_aluno (1.0,2.0,3.0,4) == Exception
assert notas_aluno (2.0,2.0,2.0,'a') == 2
assert notas_aluno('627',47,347,'p') == Exception
assert notas_aluno(2.0,2.0,2.0,'z') == False
assert notas_aluno(2.0,2.0,2.0,'p') == 6.67
assert notas_aluno(2,2,2,'p') == 6.67
assert notas_aluno (2,2,2,'a') == 2


print('ok')