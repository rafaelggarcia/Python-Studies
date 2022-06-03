primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeirotermo
c = 0
total = 0
mais = 10
while mais != 0:
    total = total + 10
    while c <= total:
        print(f'{termo}', end=' - ')
        termo += razao
        c += 1
    print('Pause')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada')
