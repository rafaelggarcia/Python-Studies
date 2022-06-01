primeirotermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeirotermo + (10 - 1) * razao
for c in range(primeirotermo, decimo + razao, razao):
    print(f'{c}', end=', ')
print('Fim')
