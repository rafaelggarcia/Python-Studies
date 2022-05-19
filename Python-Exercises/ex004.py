texto = input('Digite o texto para saber mais informações: ')

print('O texto é alfabetico?', texto.isalpha())
print('O texto é alfanúmerico?', texto.isalnum())
print('O texto é númerico?', texto.isnumeric())
print('O texto tem somente espaços?', texto.isspace())
print('O texto está em maiscula?', texto.isupper())
print('O texto está em minuscula?', texto.islower())
print('O texto pode ser impresso?', texto.isprintable())
print('O texto está capitalizado?', texto.istitle())

#print(texto.isascii())
#print(texto.isdecimal())
#print(texto.isidentifier())
