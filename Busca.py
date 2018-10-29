class Busca():
    global busca
    global max_price
    global min_price
    global categoria
    global ordenacao

    def __init__(self):
        self.busca = None
        self.max_price = None
        self.min_price = None
        self.categoria = None
        self.ordenacao = None

    def atribui_valor_maximo(self, vm):
        self.max_price = vm

    def atribui_valor_minimo(self, vm):
        self.min_price = vm

    def atribui_busca(self, b):
        self.busca = b

    def atribui_ordenacao(self, od):
        self.ordenacao = od

    def atribui_categoria(self, cat):
        self.categoria = cat
