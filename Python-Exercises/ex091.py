from random import randint
from operator import  itemgetter
p1 = randint(1, 7)
p2 = randint(1, 7)
p3 = randint(1, 7)
p4 = randint(1, 7)
todos = {'P1': p1, 'P2': p2, 'P3': p3, 'P4': p4}
for k, v in todos.items():
    print(f'O player {k} tirou {v}!')
print( '_' * 25 )
ranking = []
ranking = sorted(todos.items(), key = itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}!')
