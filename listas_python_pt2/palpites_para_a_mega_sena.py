''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
em uma lista composta.'''
import random
from time import sleep
lista = []
listajogos = []
#numeros = random.randint(1,99)
print('-=' * 30)
print(' '*15 +'JOGO DA MEGA'+' '*15 )
print('-=' *30)

pedido = int(input('quando jogos gostaria de gerar: '))
tot = 0
while tot <= pedido-1:
    cont = 0
    while True:
        numeros = random.randint(1,60)

        if numeros not in lista:
            lista.append(numeros)
            cont = cont +1
        if cont >= 6:
            break
    tot = tot + 1

    listajogos.append(lista[:])
    lista.clear()

print('gerando jogos aguarde....')
sleep(2)
print('-=-=-=-= JOGOS GERADOS -=-=-=-=')
for c,jogo in enumerate(listajogos):
    print(f'jogo {c+1}: {jogo}')
    sleep(2)
print('-=-=-=-= BOA SORTE -=-=-=-=')

