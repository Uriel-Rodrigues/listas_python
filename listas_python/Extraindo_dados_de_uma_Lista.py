'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista'''

lista = []
cont5 = 0
cont = 0
while True:

    n = int(input('digie um numero para a lista: '))
    lista.append(n)

    if n == 5:
        cont5 = cont5 + 1
    cont = cont + 1
    res = str(input('gostaria de parar SIM/NAO: ')).upper()
    if res in 'SIM':
        break
print('*-' * 20)
lista.sort()
lista.reverse()
print(f'a lista em oprdem decrescente é {lista}')
print('*='*20)
print(f'foram digitados {cont} numeros ')
print('*='*20)
for chave, valor in enumerate(lista):
    if 5 in lista:
        print(f'o numero 5 esta na lista e foi digitado {cont5}x')
        print(f'na posição: {chave}')
    else:
        print('o numero 5 não faz parte da lista')


#METODO SEM USAR O SORT E O REVERSE:

'''lista = []

while True:
    n = int(input('digite um numero para a lista: '))
    res = str(input('quer parar SIM/NAO: '))
    if res in 'SIM':
        break
    if len(lista) == 0 or n < lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos <= len(lista):
            if n >= lista[pos]:
                lista.insert(pos,n)
        pos = pos + 1


print(lista)'''