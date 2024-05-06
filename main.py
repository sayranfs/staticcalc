import math

# Introdução ao script fazendo o questionamento de qual operação deseja realizar.
way = int(input("* Selecione a operação estatística que deseja fazer. *\n"
                "[1] Média\n"
                "[2] Mediana\n"
                "[3] Desvio padrão\n"))


def med(sequence):
    sum = 0
    for i in sequence:
        sum += i
        med = sum / len(sequence)
    return med


# Primeira opção: média da sequência
if way == 1:
    seq = input("Digite a sequência que deseja calcular a média (separe com espaço):\n").split(' ')
    seqArr = [eval(i) for i in seq]
    med = med(seqArr)
    print(f"A média encontrada foi: {med}")

# Segunda opção: mediana da sequência
elif way == 2:
    seq = input("Digite a sequêcia que deseja calcular a mediana (separe com espaço):\n").split(' ')
    seqArr = [eval(i) for i in seq]
    if len(seqArr) % 2 == 1:
        center = seqArr[len(seqArr) // 2]
        print(f"A mediana encontrada foi: {center}")
    else:
        center1 = seqArr[(len(seqArr) // 2) - 1]
        center2 = seqArr[len(seqArr) // 2]
        mediana = (center1 + center2) / 2
        print(f"A mediana encontrada foi: {mediana}")

# Terceira e última opção: desvio padrão da sequência
elif way == 3:
    seq = input("Digite a sequência que deseja calcular o desvio padrão (separe com espaço):\n").split(' ')
    seqArr = sorted([eval(i) for i in seq])
    med = med(seqArr)
    soma = 0
    for i in seqArr:
        soma += abs(i - med)
    var = soma / len(seqArr)
    dp = round(math.sqrt(var), 2)
    print(f"O desvio padrão encontrado foi de: {dp}")

# Caso dê um número/caractere fora do esperado, encerra a execução
else:
    exit()