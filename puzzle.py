__author__ = 'cristiano'

from node import Node
from busca import Busca


def main():
    # iniciar = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # iniciar = [2, 8, 3, 5, 0, 6, 1, 4, 7]  # 14
    # iniciar = [0, 2, 3, 1, 7, 5, 8, 4, 6]  # 8
    iniciar = [1, 2, 3, 7, 0, 8, 6, 4, 5]  # 10
    # iniciar = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    # arvore = list()
    find = Busca()
    no = Node(iniciar, "raiz", None, 0, 0, 9)
    # arvore.extend([1, 2, 3, 4, 5, 6])
    # arvore.clear()
    # print(arvore.__len__())
    # print(iniciar.__class__)
    teste = find.busca_largura(no)
    print(teste.estado)

    # print(iniciar.index(0))
    # print(a.acao, a.pai)


if __name__ == '__main__':
    main()
