import random

def gerar_array():
    return [random.randint(-999999, 999999) for _ in range(20000)]

def ordenar_array(array):
    return sorted(array)

if __name__ == "__main__":
    array = gerar_array()
    array_ordenado = ordenar_array(array)
    print(array_ordenado[:1000])