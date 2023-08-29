'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

exp = str(input('digite a sua expressão: '))
lista1 = []
lista2 =[]

for simbolo in exp:
    if simbolo == '(':
        lista1.append('(')

    elif simbolo == ')':
        lista2.append(')')

if len(lista1) == len(lista2):
    print('sua expressão é valida')
    print(f'voce abriu {len(lista1)} e fechou {len(lista2)}')

else:
    print('sua expressão é invalida')
    print(f'voce abriu {len(lista1)} e fechou {len(lista2)} parentesis')



