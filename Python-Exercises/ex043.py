peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 >= imc < 25:
    print('Você está no pesoa ideal!')
elif 25 >= imc < 30:
    print('Você está com sobrepeso!')
else:
    print('Você está com obesidade morbida!')
