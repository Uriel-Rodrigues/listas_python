'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
 posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela'''

listanum = []

for c in range(0,5):
    n = int(input('digite um numero para adicionar a lista: '))

    if c == 0 or n > listanum[-1]:
        listanum.append(n)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos <= len(listanum):
            if n <= listanum[pos]:
                listanum.insert(pos,n)
                print(f'adicionado na posição {pos} da lista')
                break
            pos = pos+1

print(listanum)