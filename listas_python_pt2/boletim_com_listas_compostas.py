'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''
from time import sleep
nomes = list()
notas = list()
dados = list()

while True:
    nomes.append(str(input('digite o nome do aluno: ')))
    for c in range(1,3):
        notas.append(float(input(f'digite a NOTA {c}: ')))
    nomes.append(notas[:])
    media = (notas[0] + notas[1])/2
    nomes.append(media)
    notas.clear()
    dados.append(nomes[:])
    nomes.clear()

    fim = str(input('gostaria de parar? SIM/NAO: ')).strip().upper()
    if 'SIM' in fim:
        break
print('-*'*30)
print(f'{"N°":<4}{"NOME":<10}{"MEDIAS":>8}')
print('-'*30)
for i, e in enumerate(dados):
    print(f'{i:<4}{e[0]:<10}{e[2]:>8}')

print('-'*10,'VISUALIZADOR DE NOTAS','-'*10)
while True:
    posicao = int(input('digite o numero correspondente ao aluno: '))

    for p, c in enumerate(dados):
        if posicao == p:
            print(f'{c[0]}')
            print(f'NOTA-1: {dados[p][1][0]}')
            print(f'NOTA-2: {dados[p][1][1]}')
    print('--'*10)
    saida = str(input('encerrar visualizador? SIM/NAO: ')).strip().upper()
    print('--'*10)
    if 'SIM' in saida:
        break
print('encerrando visualizador....')
sleep(2)
print('<<<<< - VISUALIZADOR ENCERRADO - >>>>>')