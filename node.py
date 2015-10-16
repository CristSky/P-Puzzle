__author__ = 'cristiano'


class Node(object):
    def __init__(self, estado=None, acao=None, pai=None, custo=None, profundidade=None):
        self.estado = estado.copy()
        self.acao = acao
        self.pai = pai
        self.custo = custo
        self.profundidade = profundidade
