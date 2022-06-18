def ficha  (jog='Desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeoanto!')
    



n = str(input('Digite o nome do jogador: '))
g = int(input('Digite o número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
