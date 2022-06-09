jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
jogador['total'] = int(input('Quantas partidas foram jogadas? '))
listagols = []
for c in range(0, jogador['total']):
    listagols.append(int(input(f'Quantas gols na partida {c}? ')))
jogador['gols'] = listagols
for x, y in jogador.items():
    print(f'No campo {x} temos o valor {y}!')
n = 1
totc = 0
for c in jogador['gols']:
    print(f'Na partida {n} o jogador fez {c}')
    n += 1
    totc += c
print(f'O total de gols foi {totc}')