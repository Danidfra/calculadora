import math


def soma(n1, n2):

    resultado = n1 + n2

    return resultado

def sub(n1, n2):

    resultado = n1 - n2

    return resultado

def mult(n1, n2):

    resultado = n1 - n2

    return resultado

def div(n1, n2):

    resultado = n1 - n2

    return resultado

# def div():
operacao = list()

continuar = ''

while continuar != 'stop':

    continuar = 'continuar' if input('Continuar? S/N ').lower() in 'Ss' else 'stop'

    n = input('Número: ')
    op = input('Operação: +, -, *, / e 0 para calcular o resultado ')

    operacao.append(n)
    operacao.append(op)

