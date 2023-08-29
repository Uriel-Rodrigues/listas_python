'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
e o menor valor digitado e as suas respectivas posições na lista.'''

numeros = []
maior = 0
menor = 0
cont = 0
for c in range(0, 5):
    numeros.append(int(input(f'digite um numero para a posição {c+1}: ')))

    if c == 0:
        maior = numeros[c]
        menor = numeros[c]

    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print(f'os numeros digitados foram {numeros}')
print(f'o numero maior foi {maior} na posição: ', end='')
for p, n in enumerate(numeros):
    if n == maior:
        print(f'{p+1}...', end='')
print()
print(f'o numero menor foi {menor} na posição: ', end='')
for p, n in enumerate(numeros):
    if n == menor:
        print(f'{p+1}...', end='')
print()