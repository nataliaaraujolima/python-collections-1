# Desempacotamento Direto das Tuplas:
''' O ** é uma maneira poderosa de descompactar dicionários e passar os valores
diretamente para funções ou construtores de classes, evitando
a necessidade de passar manualmente cada argumento, tornando o código mais limpo e flexível.'''

'''
# Criando a lista de objetos sem o operador **
animes = [
    Anime(anime["nome"], anime["classificacao"], anime["ano_lancamento"])
    for anime in animes_tuples
]
'''
from dataclasses import dataclass
animes_tuples = [
    {"nome": "Naruto", "classificacao": 8.3, "ano_lancamento": 2002},
    {"nome": "One Piece", "classificacao": 9.1, "ano_lancamento": 1999},
    {"nome": "Attack on Titan", "classificacao": 9.0, "ano_lancamento": 2013},
    {"nome": "Fullmetal Alchemist: Brotherhood",
        "classificacao": 9.2, "ano_lancamento": 2009},
    {"nome": "Dragon Ball Z", "classificacao": 8.7, "ano_lancamento": 1989},
    {"nome": "Death Note", "classificacao": 9.0, "ano_lancamento": 2006}
]


@dataclass
class Anime:

    nome: str
    classificacao: float
    ano_lancamento: int


animes = [Anime(**anime) for anime in animes_tuples]

for anime in animes:
    print(f"Nome: {anime.nome}, Classificação: {anime.classificacao}, Ano de Lancamento: {anime.ano_lancamento}")
