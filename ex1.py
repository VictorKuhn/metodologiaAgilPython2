import random

def gerar_array():
    return [random.randint(-999999, 999999) for _ in range(20000)]

if __name__ == "__main__":
    resultado = gerar_array()
    print(resultado)