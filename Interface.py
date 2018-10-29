from Singleton import Singleton
from representacao import Representacao
from modulo_busca import Pesquisa
import nltk
from string import punctuation
from bd_acesso import AcessaBD
from corretor import Corretor
import re
from Busca import Busca

@Singleton
class Interface:
    
    global stopwords
    global representacao
    global bdAcesso
    global corretor
    global pesquisa

    def __init__(self):
        self.stopwords = nltk.corpus.stopwords.words('portuguese')
        self.representacao = Representacao()
        self.bdAcesso = AcessaBD()
        self.corretor = Corretor()
        self.pesquisa = Pesquisa()



    def _my_tokenizer(self, s):
        resp = ' |\n|!|"|#|$|%|&|\'|\(|\)|\*|\+|\,|\-|\.|/|:|;|<|=|>|\?|@|[|\|]|^|_|`|{|||}|~'
        words = []
        pont = list(punctuation)
        for w in re.split(resp, s):
            if w not in pont and w.lower() not in self.stopwords and len(w) > 0:
                words.append(w.lower())
        return words

    # def nova_busca (self):
    #     return Busca()


    def _representacao(self, busca):
        words = self._my_tokenizer(busca)
        words = self.corretor.corrige(words)
        return self.representacao.devolveVetor(words)


    def _ordene(self, ids, lista):
        return (list(t) for t in zip(*sorted(zip(lista, ids))))

    def _define_ordenacao(self, ordenacao, vizualizacao, preco):
        if ordenacao == 'preco':
            return preco
        return vizualizacao

    def busque_n_relacionados(self, id_produto, n):
        ids, vetores, values = self.bdAcesso.busque_produtos_categoria_de(id_produto)
        return self.pesquisa.busca_n_relacionados(values, vetores, ids, n)



    def busque(self, busca):
        _, ids = self._devolveProdutos(busca.busca, busca.min_price, busca.max_price, busca.categoria, busca.ordenacao)
        return ids

    def _devolveProdutos(self, busca, min_preco, max_preco, categoria, ordenacao):
        if categoria and max_preco and min_preco and busca:
            ids, base, vizualizacao, preco = self.bdAcesso.devolveProdutoComIntervaloDePrecoECategoria(min_preco, max_preco, categoria)
            return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
                                self._define_ordenacao(ordenacao, vizualizacao, preco))

        if categoria and max_preco and busca:
            ids, base, vizualizacao, preco = self.bdAcesso.devolveProdutosPorCategoriaComMaxPreco(max_preco, categoria)
            return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
                                self._define_ordenacao(ordenacao, vizualizacao, preco))

        if categoria and min_preco and busca:
            ids, base, vizualizacao, preco = self.bdAcesso.devolveProdutosPorCategoriaComMinPreco(min_preco, categoria)
            return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
                                self._define_ordenacao(ordenacao, vizualizacao, preco))

        if min_preco and max_preco and busca:
            ids, base, vizualizacao, preco = self.bdAcesso.devolveProdutoComIntervaloDePreco(min_preco, max_preco)
            return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
                                self._define_ordenacao(ordenacao, vizualizacao, preco))

        if categoria and busca:
            ids, base, vizualizacao, preco = self.bdAcesso.devolveProdutosPorCategoria(categoria)
            return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
                                self._define_ordenacao(ordenacao, vizualizacao, preco))

        if categoria:
            ids, base, vizualizacao, preco = self.bdAcesso.devolveProdutosPorCategoria(categoria)
            return self._ordene(ids,self._define_ordenacao(ordenacao, vizualizacao, preco))

        if busca:
            ids, base, vizualizacao, preco = self.bdAcesso.devolveProdutos()
            return self._ordene(self.pesquisa.busca_limite_distancia(self._representacao(busca), base, ids),
                                self._define_ordenacao(ordenacao, vizualizacao, preco))

        ids, base, vizualizacao, preco = self.bdAcesso.devolveProdutos()
        return ids

    def devolveNprodutosRecomendados(self, id_cliente, N):
        return self.bdAcesso.devolveNrecomendadosParaCliente(id_cliente, N)
        # busca = [self.representacao.devolveVetor(word for word in words)]
        # produtos = bdAcesso.devolveProdutoComIntervaloDePrecoECategoria(min_preco, max_preco, categoria)



# i = Interface()
# i.devolveProdutos('camesa brunca', 2, 3,'')