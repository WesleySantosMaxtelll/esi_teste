from sklearn.neighbors import NearestNeighbors
X = [[0,0], [1,1], [5,5], [-2,-2]]
Y = [[-1,-1]]
# print(X)
# X.insert(0, [10,10])
# print(X)
# nn = NearestNeighbors(2, metric='euclidean', algorithm='brute').fit(X)
# d,i = nn.kneighbors(Y)
# print(d)
# print(i)


# from sklearn.neighbors import radius_neighbors_graph
# A = radius_neighbors_graph(X, 15.5, mode='connectivity',
#                            include_self=True)

# print(A.toarray())
# a = A.toarray()[0,1:]
# print([Y[a] for a in range(len(A.toarray()[0,1:])) if A.toarray()[0,1:][a]])
# if a:
# print(a[0])
# from bd_acesso import AcessaBD
# from representacao import Representacao
# from corretor import Corretor
# import random
#
# tags = ['camiseta branca', 'blusa inverno', 'camiseta regata', 'calça jeans', 'camisa social', 'camisa social branca',
#         'calça jeans', 'calça social', 'blusa verão', 'camiseta regata', 'calça', 'camisa social azul', 'camiseta branca lisa',
#         'calça jeans', 'computador i7', 'processador i7', 'camiseta regata listrada', 'calça cáqui',
#         'camisa social manga longa', 'camiseta social', 'calça jeans', 'notebook i7', 'processador i7',
#         'blusa verão', 'camiseta regata', 'calça preta', 'laptop i7', 'camisa social', 'camisa social',
#         'camiseta social', 'calça jeans']
#
# cat = ['camisa', 'calça', 'sapato', 'eletrônico', 'blusa']
# def random_floats(low, high, size):
#     return [random.uniform(low, high) for _ in range(size)]
#
# Y = [i for i in range(len(tags))]
# preco = random_floats(15, 50, len(Y))
#
# categorias = [random.choice(cat) for _ in range(len(Y))]
# bd = AcessaBD()
# r = Representacao()
# c = Corretor()
# print(categorias)
# print(Y)
# print(preco)

# from string import punctuation
# import re
# import nltk
#
# stopwords = nltk.corpus.stopwords.words('portuguese')
# def _my_tokenizer(s):
#     resp = ' |\n|!|"|#|$|%|&|\'|\(|\)|\*|\+|\,|\-|\.|/|:|;|<|=|>|\?|@|[|\|]|^|_|`|{|||}|~'
#     words = []
#     pont = list(punctuation)
#     for w in re.split(resp, s):
#         if w not in pont and w.lower() not in stopwords and len(w) > 0:
#             words.append(w.lower())
#     return words
#
#
# for i in range(len(Y)):
#     words = _my_tokenizer(tags[i])
#     words = c.corrige(words)
#     values = r.devolveVetor(words)
#     values = values.tolist()
#     bd.inserirProduto(Y[i], categorias[i], values, preco[i])

import time

from Busca import Busca
from Interface import Interface



print('inicio')
i = Interface.instance()

print(i.busque_n_relacionados(10, 5))
#
# b = Busca()
# b.atribui_ordenacao('preco')
# b.atribui_busca('camisa')
# b.atribui_valor_maximo(90)
# b.atribui_valor_minimo(20)

# print(id(b))
# i.busque(b)
print('comeca busca')
initial_time = time.time()

# print(i.devolveNprodutosRecomendados(5, 10))

# print(len(i.busque(b)))

print('carregou')
final_time = time.time()
print('total: ' + str(final_time - initial_time) + " secs")
# c = Busca.instance()
# b.n = 'sim'
# print(b.n)
# print(c.n)

# i = Interface()

# print(i.devolveProdutos(None, None, None, 'calça'))

# bd.devolveProdutoComIntervaloDePrecoECategoria(1, 100, 'camisa')

# def _ordene(ids, lista):
#     return (list(t) for t in zip(*sorted(zip(lista, ids))))
#
# l1 = [2, 2, 5, 1, 0, 10]
# l2 = ['dois1', 'dois2', 'cinco', 'um', 'zero', 'dez']
# l1, l2 = _ordene(l2, l1)
#
# print(l1)
# print(l2)
