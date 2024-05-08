import math
import numpy as np
import matplotlib.pyplot as plt
import random as rd
plt.style.use('seaborn-v0_8')

# Introdução ao script fazendo o questionamento de qual operação deseja realizar.
way = input("* Selecione a operação estatística que deseja fazer. *\n"
            "[1] Média\n"
            "[2] Mediana\n"
            "[3] Desvio padrão\n"
            "[4] Variância\n"
            "[5] Moda\n"
            "[0] GRÁFICO (Média e desvio padrão)\n")


# ---------- Funções ----------
# Função para calcular média usando a lista com números;
def med(sequence: list):
    sum = 0
    for i in sequence:
        sum += i
    return sum / len(sequence)


# Função para calcular a variância da sequência usando a média e a sequência de desvios;
def var(med, desvios: list):
    sum = 0
    for i in desvios:
        sum += (i - med)**2
    return sum / len(desvios)


# Função para introduzir o script de forma prática;
def intro(nome: str):
    sequence = input(f"Digite a sequência que deseja calcular {nome} ou digite 'rand' para gerar aleatoriamente! (separe com espaço):\n").split(' ')
    if sequence == ['rand']:
        rand = [rd.randint(0, 100) for i in range(30)]
        print(rand)
        return rand
    else:
        x = sequence.count('')
        i = 0
        while i < x:
            sequence.remove('')
            i += 1
        return list(np.array(sequence, dtype=int))


# Função para o cálculo da moda da sequência;
def moda(sequence: list, tipo: int):
    qnt = []
    norepeat = []
    mo = []
    for i in sequence:
        if not i in norepeat:
            qnt.append(sequence.count(i))
            norepeat.append(i)
    y = qnt.copy()
    for i in y:
        if i == max(y):
            mo.append(norepeat.pop(qnt.index(max(y))))
            qnt.pop(qnt.index(max(y)))
    if tipo == 1:
        return mo
    if tipo == 2:
        if not len(norepeat):
            return 'AMODAL'

        elif len(mo) == 1:
            return 'UNIMODAL'

        elif len(mo) == 2:
            return 'BIMODAL'

        elif len(mo) > 2:
            return 'MULTIMODAL'
    if tipo == 3:
        return max(y)


# Função que calcula a mediana da sequência;
def mediana(sequence: list):
    if len(sequence) % 2 == 1:
        return sequence[len(sequence) // 2]
    else:
        center1 = sequence[(len(sequence) // 2) - 1]
        center2 = sequence[len(sequence) // 2]
        return (center1 + center2) / 2


# Função auxiliar da construção do gráfico.
def plotar(x, txt: str):
    plt.plot(np.linspace(x, x))
    plt.text(0, x, f"{txt} {round(x, 2)}", c="red", fontsize=12)




# ---------- Código ----------
# Primeira opção: média da sequência;
if way == '1':
    seq = intro("a MÉDIA")
    print(f"A média encontrada foi: {round(med(seq), 2)}.")


# Segunda opção: mediana da sequência;
elif way == '2':
    seq = intro("a MEDIANA")
    print(f"A mediana encontrada foi: {mediana(seq)}.")

# Terceira opção: desvio padrão da sequência;
elif way == '3':
    seq = intro("o DESVIO PADRÃO")
    print(f"O desvio padrão encontrado foi de: {round(math.sqrt(var(med(seq), seq)), 2)}.")


# Quarta opção: variância da sequência;
elif way == '4':
    seq = intro("a VARIÂNCIA")
    print(f"A variância encontrado foi de: {round(var(med(seq), seq), 2)}.")


# Quinta opção: moda da sequência.
elif way == '5':
    seq = intro("a MODA")
    nums = moda(seq, 1)
    title = moda(seq, 2)
    rep = moda(seq, 3)
    if title == 'AMODAL':
        print("A sequência é AMODAL, não possuindo moda.")
    else:
        print(f"A sequência é {title} com a(s) moda(s) sendo {nums} se repetindo {rep} vezes.")


# Sexta opção: construção de gráfico com informações.
elif way == '0':
    seq = intro("o GRÁFICO")
    x = []
    for i in range(len(seq)):
        x.append(i)
    dp = math.sqrt(var(med(seq), seq))
    plt.scatter(x, np.array(seq))
    plotar(med(seq), "Média:")
    plotar(med(seq) + dp, "Média + DP:")
    plotar(med(seq) - dp, "Média - DP:")
    plotar(mediana(seq), "Mediana:")
    plt.show()

# Caso dê um número/caractere fora do esperado, encerra a execução.
else:
    exit()