primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeirotermo
c = 0
while c <= 10:
    print(f'{termo}', end='')
    termo += razao
    c += 1
print('Fim')
