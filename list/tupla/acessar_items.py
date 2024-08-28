animes = [
    {"nome": "Naruto", "classificacao": 8.3, "ano_lancamento": 2002},
    {"nome": "One Piece", "classificacao": 9.1, "ano_lancamento": 1999},
    {"nome": "Attack on Titan", "classificacao": 9.0, "ano_lancamento": 2013},
    {"nome": "Fullmetal Alchemist: Brotherhood",
        "classificacao": 9.2, "ano_lancamento": 2009},
    {"nome": "Dragon Ball Z", "classificacao": 8.7, "ano_lancamento": 1989},
    {"nome": "Death Note", "classificacao": 9.0, "ano_lancamento": 2006}
]


anime_tupla = [
    (anime['nome'], anime['classificacao'])
    for anime in animes
]

print(anime_tupla)
