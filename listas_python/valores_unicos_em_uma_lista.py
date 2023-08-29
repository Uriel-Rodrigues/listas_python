'''Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
exibidos todos os valores únicos digitados, em ordem crescente.'''

res = ''
listanum = []
while True:
    numero = int(input('digite um numero para alista: '))

    if numero not in listanum:
        listanum.append(numero)
    else:
        print('\nvalor ja existente na lista')
        novonumero = int(input('digite um novo numero: '))
        while novonumero in listanum:
            novonumero = int(input('digite um novo numero: '))
        if novonumero not in listanum:
            listanum.append(novonumero)

    res = str(input('deseja sair? SIM/NAO')).upper()
    if res in 'SIM':
        break
print('*-*-'*20)
listanum.sort()
print(f'os numeros digitados em ordem crescente foram: {listanum}')