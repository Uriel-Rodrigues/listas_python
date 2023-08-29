'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
parcont = 0
colcont = 0
maior = menor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz [l][c] = int(input(f'digite um numero par a linha {l} coluna {c}: '))

        if matriz[l][c]%2 == 0:
            parcont = parcont + matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            colcont = colcont + matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maior = menor = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[1][c] < menor:
            menor = matriz[1][c]

print('#=' *30)
print('-*-*-*-*-*- VEJA SUA MATRIZ -*-*-*-*-*-')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()

print('-*-*-*-*-*- SOMA DOS PARES -*-*-*-*-*-')
print(f'a soma dos numeros pares for {parcont}')
print()
print('-*-*-*-*-*- SOMA VALORES 3° COLUNA -*-*-*-*-*-')
print(f'a soma dos valores da terceira coluna é: {colcont}')
print()
print(f'-*-*-*-*-*- MANIOR VALOR 2° LINHA -*-*-*-*-*-')
print(f'o maior valor da 2° linha é: {maior}')