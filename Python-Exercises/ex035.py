a = float(input('Digite o valor da reta: '))
b = float(input('Digite o valor da reta: '))
c = float(input('Digite o valor da reta: '))

if a < b * c and b < a + c and c < a + b:
    print('Os seguimentos acima podem formar um triângulo!')
else:
    print('Os seguimentos acima não formam um triângulo!')


print(3 * 5 + 4 ** 2)