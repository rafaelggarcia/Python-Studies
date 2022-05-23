distancia = float(input("Digite a distância da viagem em KM's: "))
if distancia <= 200:
    valor = distancia * 0.50
    print(f'Sua viagem custa {valor:.2f} R$')
else:
    valor = distancia * 0.45
    print(f'Sua viagem custa {valor:.2f} R$')
print('Tenha uma boa viagem!')