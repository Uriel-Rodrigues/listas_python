'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas.'''

listageral = []
listapar = []
listaimpar = []

while True:
    numero = int(input('digite o numero para a lista: '))

    listageral.append(numero)

    if numero%2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)

    res = str(input('gostaria de parar? SIM/NAO: ')).upper()

    if res in 'SIM':
        break
print('---------- LISTAD GERADAS ----------' )
print(f'[1] lista geral: {listageral}')
print(f'[2] lista par: {listapar}')
print(f'[3] lista impar: {listaimpar}')
print('------------------------------------')