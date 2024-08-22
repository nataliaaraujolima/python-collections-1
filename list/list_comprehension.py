'''permite que você construa uma nova lista aplicando uma expressão a cada item
de uma sequência ou coleção existente,
opcionalmente filtrando elementos com base em uma condição.
sintaxe -> [nova_expressao for item in coleção if condição]
'''

animes = [
    {"nome": "Naruto", "classificacao": 8.3, "ano_lancamento": 2002},
    {"nome": "One Piece", "classificacao": 9.1, "ano_lancamento": 1999},
    {"nome": "Attack on Titan", "classificacao": 9.0, "ano_lancamento": 2013},
    {"nome": "Fullmetal Alchemist: Brotherhood",
        "classificacao": 9.2, "ano_lancamento": 2009},
    {"nome": "Dragon Ball Z", "classificacao": 8.7, "ano_lancamento": 1989},
    {"nome": "Death Note", "classificacao": 9.0, "ano_lancamento": 2006}
]

# Objetivo: Criar uma nova lista com os nomes dos animes que têm uma classificação maior que 9.0.


def filtra_alta_classificação(anime):
    """
    Determines if an anime has a rating higher than 8.9.

    Args:
        anime (dict): An anime object containing a rating.

    Returns:
        bool: True if the anime's rating is higher than 8.9, False otherwise.
    """
    return anime["classificacao"] > 8.9


resultado_classificacao = [
    anime["nome"]
    for anime in animes
    if filtra_alta_classificação(anime)]
print(resultado_classificacao)
