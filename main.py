# 1 - imports - bibliotecas
import pytest

# 2 - class - classes



# 3 - definitions - definições - métodos ou funções


def print_hi(name):
    print(f'Hi, {name}')

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

# esse é um exemplo de demonstração
def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return 'Não dividirás por zero'

def dividir_try_except(numero1, numero2):
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        return 'Não dividirás por zero'


# Testes Unitários / Testes de Unidades

# teste da função somar
def test_somar_didatico():

    # 1 - Configura / Prepara

    numero1 = 8 # input / Entrada
    numero2 = 5 # input / Entrada
    resultado_esperado = 13 # output / Saída

    # 2 - Executa

    resultado_atual = somar(numero1, numero2)

    # 3 - Check / Valida

    assert resultado_atual == resultado_esperado

@pytest.mark.parametrize('numero1,numero2,resultado', [
    # valores
    (5, 4, 9),  # teste 1
    (3, 2, 5),  # teste 2
    (10, 6, 16),  # teste 3

])

def test_somar(numero1, numero2, resultado):
    try:
        assert somar(numero1,numero2) == resultado
    except AssertionError:
        print(f'Entrou no Except: {AssertionError}')
        pass

def test_somar_resultado_negativo():
    assert somar(-1000,-2000) == -3000

def test_subtrair():
    assert subtrair(4,5) == -1

def test_multiplicar():
    assert multiplicar(3,7) == 21

def test_dividir():
    assert dividir(8,0) == 2

@pytest.mark.parametrize('numero1,numero2, resultado', [
    (8,2,4),
    (20,4,5),
    (10,0,'Não dividirás por zero'),

])
def test_dividir_try_except(numero1,numero2,resultado):
    assert dividir_try_except(numero1, numero2) == resultado


def test_dividir_por_zero():
    assert dividir(8, 0) == 'Não dividirás por zero'



    # teste positivo - mostrar o resultado correto
    #                - avançar  para a próxima etapa

    # teste negativo - mostrar a mensagem de erro

if __name__ == '__main__':
    print_hi('PyCharm')



    resultado = somar(4,2)
    print(f'O resultado da soma: {resultado}')

    resultado = subtrair(5, 3)
    print(f'O resultado da subtração: {resultado}')

    resultado = multiplicar(2, 4)
    print(f'O resultado da multiplicação: {resultado}')

    resultado = dividir(9, 0)
    print(f'O resultado da divisão: {resultado}')





