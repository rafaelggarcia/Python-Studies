times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza',
         'Bragantino','Athletico-PR', 'Internacional', 'Fluminense',
         'Atlético-GO', 'Cuiabá', 'Ceará', 'São Paulo', 'América-MG',
         'Juventude', 'Santos', 'Bahia', 'Sport', 'Grêmio', 'Chapecoense')
print(f'Os 5 primeiros colocados são {times[0:5]}')
print(f'Os 5 últimos colocados são {times[-4:]}')
print(f'Os times em ordem alfabéticas são {sorted(times)}!')
print(f'A Chapecoense está na posição: {times.index("Chapecoense")+1}!')