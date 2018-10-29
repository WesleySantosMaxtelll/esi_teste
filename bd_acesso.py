import psycopg2
import datetime


class AcessaBD():
    global conn
    global cur

    def __init__(self):
        self.conn = psycopg2.connect("dbname=esifr user=postgres password=Alphabet@6494 host=localhost")
        self.cur = self.conn.cursor()

    def inserirBusca(self, idCliente, busca):
        self.cur.execute("insert into buscas (idCliente, busca, dt) values (%s, %s, %s)",
                         (idCliente, busca, datetime.datetime.now()))
        self.conn.commit()

    def devolveBuscasRecentesCliente(self, idCliente, N):
        self.cur.execute("select busca from buscas where idCliente = " + str(idCliente)
                         + " order by dt desc limit " + str(N) + ";")
        return self.cur.fetchall()

    def devolveBuscasRecentesSemLogin(self, N):
        self.cur.execute("select busca from buscas order by dt desc limit " + str(N) + ";")
        return self.cur.fetchall()

    # Pesquisa por categoria
    def inserirProduto(self, idProduto, categoria, arrayTAG, preco):
        self.cur.execute("insert into produto (idProduto, categoria, arrayTAG, preco) " +
                         "values (%s, %s, %s, %s)", (idProduto, categoria, arrayTAG, preco))
        self.conn.commit()


    def atualizeProdutoPreco(self, idProduto, preco):
        self.cur.execute("update produto set preco = " + str(preco) + " where idProduto =" + str(idProduto) + ";")
        self.conn.commit()


    def atualizeProdutoTags(self, idProduto, arrayTAG):
        self.cur.execute(
            "update produto set arrayTAG = \'" + str(arrayTAG) + "\' where idProduto =" + str(idProduto) + ";")
        self.conn.commit()


    def atualizeProdutoCategoria(self, idProduto, categoria):
        self.cur.execute(
            "update produto set categoria = \'" + categoria + "\' where idProduto =" + str(idProduto) + ";")
        self.conn.commit()


    def devolveProdutos(self):
        self.cur.execute("select idProduto, arrayTAG, vizualizado, preco from produto order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    def devolveProdutosPorCategoria(self, categoria):
        self.cur.execute(
            "select idProduto, arrayTAG, vizualizado, preco from produto where categoria = \'" + categoria + "\' order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    def devolveProdutoComIntervaloDePreco(self, min_preco, max_preco):
        self.cur.execute("select idProduto, arrayTAG, vizualizado, preco from produto where preco between "
                         + str(min_preco) + " and " + str(max_preco) + " order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    def devolveProdutosPorCategoriaComMinPreco(self, min_preco, categoria):
        self.cur.execute("select idProduto, arrayTAG, vizualizado, preco from produto where categoria = \'" + categoria + "\' and "
                         + "preco >= "+ str(min_preco) + " order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    def devolveProdutosPorCategoriaComMaxPreco(self, max_preco, categoria):
        self.cur.execute("select idProduto, arrayTAG, vizualizado, preco from produto where categoria = \'" + categoria + "\' and "
                         + "preco <= "+ str(max_preco) + " order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    def devolveProdutoComIntervaloDePrecoECategoria(self, min_preco, max_preco, categoria):
        self.cur.execute("select idProduto, arrayTAG, vizualizado, preco from produto where categoria = \'" + categoria + "\' and "
                         + "preco between " + str(min_preco) + " and " + str(max_preco) + " order by vizualizado desc;")
        resp = self.cur.fetchall()
        return [i[0] for i in resp], [i[1] for i in resp], [i[2] for i in resp], [i[3] for i in resp]


    # Recomendacoes
    def devolveNrecomendadosParaCliente(self, id_cliente, n):
        self.cur.execute(
            "select DISTINCT idproduto from (select DISTINCT v.idcliente from " +
            "(select idProduto from visualizacao where idcliente = "+str(id_cliente)+") as t1 " +
            "join visualizacao v on t1.idproduto = v.idproduto where v.idcliente !="+str(id_cliente)+") as innertab "+
            "join visualizacao v on innertab.idcliente = v.idcliente and idproduto not in "+
            "(select idproduto from visualizacao where idcliente ="+str(id_cliente)+") limit "+str(n)+";")
        return [f[0] for f in self.cur.fetchall()]

# bd = AcessaBD()
        # print(bd)
        # bd.inserir('2', 'outra vez')
# bd.inserirProduto(6, 'blusa', [1.00000002,-2.25896354,3,5,9,1,2,3,5,5,2,2,3,5,9,1,2,3,5,5,2,2,3,5,
# 9,1,2,3,5,5,2,2,3,5,9,1,2,3,5,5,2,2,3,5,9,1,2,3,5,5],20.20)
# rows = bd.devolveBuscasRecentesCliente(2, 2)

# a = [1.00000002,-2.25896354,3,5,9,1,2,3,5,5,2,2,3,5,9,1,2,3,5,5,2,2,3,5,
# 9,1,2,3,5,5,2,2,3,5,9,1,2,3,5,5,2,2,3,5,9,1,2,3,5,5]
# print(type(a))

# bd.atualizeProdutoTags(6, [0.55556, 1.00004484])
# rows = bd.devolveProdutoComIntervaloDePreco(30, 100)
# rows = bd.devolveProdutosPorCategoria('blusa')
# for row in rows:
# 	print (row)
        	# print(rows)
