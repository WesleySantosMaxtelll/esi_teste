import numpy as np
import random


nPessoas = 20
nPontos = 39

X = np.array(   [40, 32, 25, 22, 18, 17, 15, 18, 20,20, 
                 18, 18, 19, 15, 12, 9, 7, 10,10, 11, 
                 5, 8, 10, 4, 3, 4, 6,10, 8, 12, 
                 19, 15, 12, 9, 7, 10, 9, 12])
Y = np.array([X[0]])
passageiros = np.zeros(38)
for i in range(1, nPontos-1):
    aux = np.array([Y[i-1]+X[i]])
    Y = np.append(Y, aux)

# print(Y)
# print(X)


soma = sum(X)
for p in range(nPessoas):
    pos = random.randint(0, soma)
    for v in range(nPontos-1):
        if v == 0:
            if pos <= Y[v] and v ==0:
                passageiros[0] +=1

        elif pos <= Y[v] and pos > Y[v-1]:
            passageiros[v] +=1

print(passageiros)
    # print(pos)
#                            0, 1, 2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23
horariosDePico = np.matrix([[3, 1, 0, 3,15,15,13,10, 6, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 5, 7, 2, 1, 0], #0
                            [1, 2, 0, 1,10,14,10, 8, 7, 3, 2, 1, 2, 2, 1, 1, 2, 3, 2, 1, 2, 1, 1, 0], #1
                            [1, 2, 0, 1, 9,14,10, 6, 8, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 2, 1, 1, 0], #2
                            [1, 2, 0, 1, 5,12, 8, 6, 8, 2, 1, 1, 2, 1, 2, 3, 2, 3, 2, 1, 2, 1, 1, 0], #3
                            [1, 2, 0, 1, 4, 9,11, 8, 8, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 2, 1, 1, 0], #4
                            [1, 2, 0, 1, 4, 9,11, 8, 8, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 2, 1, 1, 0], #5
                            [1, 2, 0, 1, 4, 9,11, 8, 8, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 2, 1, 1, 0], #6
                            [1, 2, 0, 1, 4, 9,11, 8, 8, 2, 1, 1, 2, 2, 4, 5, 2, 3, 2, 1, 2, 1, 1, 0], #7
                            [0, 1, 2, 1, 4, 9,11, 8, 8, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #8
                            [0, 2, 2, 1, 4, 9,11, 8, 8, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #9
                            [0, 1, 2, 1, 4, 9,11, 8, 8, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #10
                            [0, 1, 2, 1, 4, 9,11, 8, 8, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #11
                            [0, 2, 2, 1, 4, 9,11, 8, 8, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #12
                            [0, 1, 2, 1, 2, 6,15, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #13
                            [0, 2, 2, 1, 2, 4,16, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #14
                            [0, 2, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #16
                            [0, 1, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #15
                            [0, 2, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #17
                            [0, 1, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #18
                            [0, 3, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #19
                            [0, 1, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #20
                            [0, 3, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #21
                            [2, 2, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #22
                            [1, 1, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #23
                            [0, 3, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 1, 2, 1, 4, 3, 2, 0], #24
                            [1, 1, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 5, 1, 2, 4, 3, 2, 0], #25
                            [0, 3, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 5, 1, 1, 4, 3, 2, 0], #26
                            [1, 1, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 5, 2, 6, 4, 3, 2, 0], #27
                            [0, 3, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 5, 1, 1, 4, 3, 2, 0], #28
                            [0, 2, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 5, 4, 1, 1, 3, 2, 0], #29
                            [1, 3, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 5, 5, 1, 1, 3, 2, 0], #30
                            [0, 2, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 5, 1, 6, 4, 3, 2, 0], #31
                            [0, 2, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 1, 2, 5, 1, 3, 1, 1, 2, 0], #32
                            [0, 1, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 2, 2, 5, 2, 3, 1, 1, 2, 0], #33
                            [0, 1, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 1, 2, 5, 2, 3, 1, 1, 2, 0], #34
                            [2, 3, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 2, 2, 2, 3, 2, 1, 1, 2, 0], #35
                            [1, 1, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 5, 5, 2, 1, 1, 2, 0], #36
                            [1, 3, 2, 1, 2, 4, 3, 9, 6, 5, 3, 6, 8, 2, 1, 3, 2, 5, 1, 2, 1, 1, 2, 0], #37

                        ])
# print(np.array(horariosDePico[1]).ravel())

distribuicaoPassageiros = np.zeros((38, 24))
# print(distribuicaoPassageiros)

for ponto in range(len(Y)):
    vetor = np.array(horariosDePico[ponto]).ravel()
    somaHP = sum(vetor)
    Y = np.array([vetor[0]])
    for i in range(1, 24):
        aux = np.array([Y[i - 1] + vetor[i]])
        Y = np.append(Y, aux)
    # print(Y)
    # print(somaHP)

    for p in range(int(passageiros[ponto])):
        pos = random.randint(0, somaHP)
        for v in range(24):
            if v == 0:
                if pos <= Y[v] and v == 0:
                    distribuicaoPassageiros[ponto,0] += 1
            elif pos <= Y[v] and pos > Y[v - 1]:
                distribuicaoPassageiros[ponto, v] += 1

#
# for i in range(2, 10):
#     x = np.random.chisquare(i,4)
#
#     print(x)

def devolveDestino(pontoAtual, sorteado):
    return 38 - int(sorteado/(7/(38-pontoAtual)))


import matplotlib.pyplot as plt
pont = np.random.noncentral_chisquare(2, .00000010,size=1000000)
values = plt.hist(pont, bins=200, density=True, color='crimson')
# plt.show()

listFinal = [i for i in pont if i < 7]

unidade = 12 #quantas unidades por minuto

# print(listFinal)
print(devolveDestino(5, 6.9))

saida = open('/home/maxtelll/Documents/USP/sextoSemestre/rp2/passageiros.txt', 'w+')

print('horario\tchegada\tdestino')

for i in range(38):
    ponto = np.array(distribuicaoPassageiros[i]).ravel()
    print(ponto)
    for auxHorario in range(len(ponto)):
        print(auxHorario)
        for d in range(int(ponto[auxHorario])):
            horarioDeChegada = random.uniform(auxHorario*60*unidade, (1.0+auxHorario)*60*unidade)
            s = str(int(horarioDeChegada)) + ';'+str(i)+';'+str(devolveDestino(i, random.choice(listFinal)))
            print(s)
            saida.write(s+'\n')

saida.close()

# fazer gerador de onibus e pontos
# max = 23*60*unidade

# saidaOnibus = open('/home/maxtelll/Documents/USP/sextoSemestre/rp2/onibus.txt', 'w+')
# saidaEntrePontos = open('/home/maxtelll/Documents/USP/sextoSemestre/rp2/temposEntrePontos.txt', 'w+')
# saidaParadas = open('/home/maxtelll/Documents/USP/sextoSemestre/rp2/temposParadas.txt', 'w+')
# for _ in range(10):
#     t = random.randint(10, 10*unidade)
#     saidaParadas.write(str(t)+'\n')

# saidaParadas.close()


# for novoOnibus in range(60):
#     inicio = random.randint(*novoOnibus*max/64, max)



# import scipy.optimize
#
# def parabola(x, a, b, c):
#     return a*x**2 + b*x + c
#
# params = [1, -5, 10]
# x = np.linspace(-5, 5, 31)
# y = parabola(x, params[0], params[1], params[2])
# plt.plot(x, y, label='analytical')
# plt.legend(loc='lower right')
# # plt.show()
#
# r = np.random.RandomState(42)
# y_with_errors = y + r.uniform(-1, 1, y.size)
# plt.plot(x, y_with_errors, label='sample')
# plt.legend(loc='lower right')
# plt.show()