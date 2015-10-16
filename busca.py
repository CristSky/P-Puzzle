__author__ = 'cristiano'
from node import Node


class Busca(object):
    def __init__(self):
        self.pilha_fila = list()

    def teste_objetivo(self, estado):
        self.objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        if self.objetivo == estado:
            return True
        else:
            return False

    def sucessor(self, aux):
        index = aux.estado.index(0)
        posY = index % 3
        mov = aux.before_index - index

        if index < 3:
            self.pilha_fila.append(self.up(aux, index))
        elif index < 6:
            if mov != 3:
                self.pilha_fila.append(self.up(aux, index))
            if mov != -3:
                self.pilha_fila.append(self.down(aux, index))
        else:
            self.pilha_fila.append(self.down(aux, index))

        if posY == 0:
            self.pilha_fila.append(self.left(aux, index))
        elif posY == 1:
            if mov != 1:
                self.pilha_fila.append(self.left(aux, index))
            if mov != -1:
                self.pilha_fila.append(self.right(aux, index))
        else:
            self.pilha_fila.append(self.right(aux, index))

    def up(self, pai, i):
        new = Node(pai.estado, 'up', pai, pai.custo + 1, pai.profundidade + 1, i)
        new.estado[i] = new.estado[i + 3]
        new.estado[i + 3] = 0
        return new

    def down(self, pai, i):
        new = Node(pai.estado, 'down', pai, pai.custo + 1, pai.profundidade + 1, i)
        new.estado[i] = new.estado[i - 3]
        new.estado[i - 3] = 0
        return new

    def left(self, pai, i):
        new = Node(pai.estado, 'left', pai, pai.custo + 1, pai.profundidade + 1, i)
        new.estado[i] = new.estado[i + 1]
        new.estado[i + 1] = 0
        return new

    def right(self, pai, i):
        new = Node(pai.estado, 'right', pai, pai.custo + 1, pai.profundidade + 1, i)
        new.estado[i] = new.estado[i - 1]
        new.estado[i - 1] = 0
        return new

    def busca_largura(self, raiz):
        self.pilha_fila.append(raiz)
        while self.pilha_fila.__len__() != 0:
            aux = self.pilha_fila.pop(0)
            # print('\n',aux.estado[0],aux.estado[1],aux.estado[2],'\n',aux.estado[3],aux.estado[4],aux.estado[5],'\n',aux.estado[6],aux.estado[7],aux.estado[8], aux.acao,aux.custo)
            if self.teste_objetivo(aux.estado):
                return aux
            else:
                self.sucessor(aux)
        return raiz
