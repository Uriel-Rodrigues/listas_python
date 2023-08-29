'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas  mais pesadas.
C) Uma listagem com as pessoas'''

cadastros = []
dados = []
pmaior = pmenor = 0

print('*='*20)
print('cadastro de pessoas')
print('*='*20)
while True:
    dados.append(str(input('NOME: ')))
    dados.append(float(input('PESO: ')))

    if len(cadastros) == 0:
        pmaior = pmenor = dados[1]
    else:
        if dados[1] > pmaior:
            pmaior = dados[1]
        if dados[1] < pmenor:
            pmenor = dados[1]
    cadastros.append(dados[:])
    dados.clear()

    res = str(input('gostaria de parar? SIM/NAO: ')).upper()

    if res in 'SIM':
        break

print('-*-*-*-*-*- NUMERO DE PESSOAS -*-*-*-*-*-')
print(f'foram cadastradas {len(cadastros)} pessoas')

print('\n-*-*-*-*-*- LISTA DOS CADASTRADOS -*-*-*-*-*-')
for pessoa in cadastros:
    print(f'-NOME:{pessoa[0]}.....PESO:{pessoa[1]}')

print('-*-*-*-*-*- PESSOAS MAIS PESADAS -*-*-*-*-*-')

print(f'o maior peso foi de {pmaior} ',end='')
for p in cadastros:
    if p[1] == pmaior:
        print(f'que é o peso de: {p[0]}')
print(f'o menor peso foi de {pmenor} ',end='')
for p in cadastros:
    if p[1] == pmenor:
        print(f'que é o peso de: {p[0]}')
