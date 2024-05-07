import math
import numpy as np

# Introdução ao script fazendo o questionamento de qual operação deseja realizar.
way = input("* Selecione a operação estatística que deseja fazer. *\n"
                "[1] Média\n"
                "[2] Mediana\n"
                "[3] Desvio padrão\n"
                "[4] Variância\n"
                "[5] Moda\n")


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
        sum += abs(i - med)
    return sum / len(desvios)


# Função para introduzir o script de forma prática;
def intro(nome: str):
    seq = input(f"Digite a sequência que deseja calcular {nome} (separe com espaço):\n").split(' ')
    x = seq.count('')
    i = 0
    while i < x:
        seq.remove('')
        i += 1
    return list(np.array(seq, dtype=int))

# Função para o cálculo da moda da sequência.
def moda(seq: list, tipo: int):
    qnt = []
    norepeat = []
    mo = []
    for i in seq:
        if not i in norepeat:
            qnt.append(seq.count(i))
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


# ---------- Código ----------
# Primeira opção: média da sequência;
if way == '1':
    seq = intro("a MÉDIA")
    print(f"A média encontrada foi: {med(seq)}.")

# Segunda opção: mediana da sequência;
elif way == '2':
    seq = intro("a MEDIANA")
    if len(seq) % 2 == 1:
        center = seq[len(seq) // 2]
        print(f"A mediana encontrada foi: {center}.")
    else:
        center1 = seq[(len(seq) // 2) - 1]
        center2 = seq[len(seq) // 2]
        mediana = (center1 + center2) / 2
        print(f"A mediana encontrada foi: {mediana}.")

# Terceira opção: desvio padrão da sequência;
elif way == '3':
    seq = intro("o DESVIO PADRÃO")
    dp = round(math.sqrt(var(med(seq), seq)), 2)
    print(f"O desvio padrão encontrado foi de: {dp}.")

# Quarta opção: variância da sequência;
elif way == '4':
    seq = intro("a VARIÂNCIA")
    print(f"A variância encontrado foi de: {var(med(seq), seq)}.")

# Quinta e última opção: moda da sequência.
elif way == '5':
    seq = intro("a MODA")
    nums = moda(seq, 1)
    title = moda(seq, 2)
    rep = moda(seq, 3)
    if title == 'AMODAL':
        print(f"A sequência é AMODAL, não possuindo moda.")
    else:
        print(f"A sequência é {title} com a(s) moda(s) sendo {nums} se repetindo {rep} vezes.")

# Caso dê um número/caractere fora do esperado, encerra a execução.
else:
    exit()