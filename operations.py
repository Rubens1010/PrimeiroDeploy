def adicionar(a, b):
    try:
        return a + b
    except TypeError:
        raise TypeError("Erro: Tipo de dados inválido.")

def subtrair(a, b):
    try:
        return a - b
    except TypeError:
        raise TypeError("Erro: Tipo de dados inválido.")

def multiplicar(a, b):
    try:
        return a * b
    except TypeError:
        raise TypeError("Erro: Tipo de dados inválido.")

def dividir(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Erro: Não é possível dividir por zero.")
        return a / b
    except TypeError:
        raise TypeError("Erro: Tipo de dados inválido.")
