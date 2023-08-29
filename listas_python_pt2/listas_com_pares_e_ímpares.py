'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = [[],[]]
numero = 0
for n in range(0, 7):
    numero = int(input('digite um numero para a lista: '))
    if numero%2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()
print('*=*' * 20)
print(f'os numeros pares em ordem crescente foram: {lista[0]}')
print(f'os numeros impares em ordem crescente foram: {lista[1]}')