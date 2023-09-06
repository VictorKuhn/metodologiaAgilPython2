def converter_massa_lunar(massa_terrestre):
    if massa_terrestre < 0:
        raise ValueError("A massa terrestre não pode ser negativa.")
    return massa_terrestre / 6

def converter_distancia_marte(metros_terrestres):
    if metros_terrestres < 0:
        raise ValueError("A distância em metros não pode ser negativa.")
    gravidade_terra = 9.81
    gravidade_marte = 3.71
    return (gravidade_terra / gravidade_marte) * metros_terrestres