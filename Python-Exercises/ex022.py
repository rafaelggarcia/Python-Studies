nome = str(input('Digite seu nome: ')).strip()

print(f'Seu nome maiusculo é {nome.upper()}')
print(f'Seu nome minisculo é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
nome = nome.split()
print(f'O seu primeiro nome tem {len(nome[0])}')
