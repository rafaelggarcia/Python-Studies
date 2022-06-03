from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')


#Ou pode ser feito assim matematicamente

#hi = (co ** 2 + ca ** 2) ** (1/2)