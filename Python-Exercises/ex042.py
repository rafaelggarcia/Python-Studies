s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1+s3 and s3 < s1+s2:
    if s1 == s2 and s2 == s3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')