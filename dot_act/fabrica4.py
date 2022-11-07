'''4. Faça uma função que recebe por parâmetro o tempo de duração de um
processo em uma fábrica expressa em segundos e retorna também por
parâmetro esse tempo em horas, minutos e segundos.'''

def duracao_fabrica(tempo):
    if type(tempo) != int or tempo <= 0:
        return Exception
    th = tempo // 3600
    tm = (tempo % 3600) // 60
    ts = (tempo % 3600) % 60

    return th,tm,ts


assert duracao_fabrica(3600) == (1,0,0)
assert duracao_fabrica(0) == Exception
assert duracao_fabrica(4500) == (1,15,0)
assert duracao_fabrica(8200) == (2,16,40)
assert duracao_fabrica(-754) == Exception
assert duracao_fabrica('8200') == Exception

print('ok')