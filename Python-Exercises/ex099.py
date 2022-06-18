def maior(* val):
    maior = 0
    if len(val) <= 1:
        maior = val[1]
    else:
        for i in val:
            if i > maior:
                maior = i
    print(f'Analisando os valores passados!')
    print(f'Foram informados {len(val)} valores ao todos.')
    print(f'O maior valor é {maior}!')
    print('=' * 30)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)