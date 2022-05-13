#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class Aresta:
    def __init__(self, vertice1, peso, vertice2):
        self.vertice1 = vertice1
        self.peso = peso
        self.vertice2 = vertice2

class Vertice:
    def __init__(self, nome):
        self.nome = nome

class Grafo:
    def __init__(self, qtdVertices):
        self.qtdVertices = qtdVertices
        self.matrizArestas = None
    def gerarMatriz(self, matriz):
        mtz = []
        linhaMatriz = 0
        colunaMatriz = 0
        for linha in matriz:
            mtz.append([])
            for coluna in linha:
                mtz[linhaMatriz].append(None)
                if coluna != str(0):
                    vertice1 = Vertice(alfabeto[linhaMatriz])
                    vertice2 = Vertice(alfabeto[colunaMatriz])
                    mtz[linhaMatriz][colunaMatriz]= Aresta(vertice1,coluna,vertice2)
                    colunaMatriz += 1
                else:
                    colunaMatriz += 1
            linhaMatriz += 1
            colunaMatriz = 0
        self.matrizArestas = mtz


def Prim(grafo):
    Mst = [[]*grafo.qtdVertices]
    linhaMatriz = 0
    colunaMatriz = 0
    listaPesos = [] 
    for linha in grafo.matrizArestas:
        for coluna in linha:
            if coluna.peso != 0:
                pass
    return Mst

entrada = open('L11Q1_in.txt', 'r')
lista_arvores = []
for linha in entrada:
    lista_arvores.append(linha.split())
entrada.close

g1 = Grafo(9)
g1.gerarMatriz(lista_arvores)
for l in g1.matrizArestas:
    for c in l:
        if c:
            print(f"{c.vertice1.nome}-{c.peso}-{c.vertice2.nome} ", end="")
        else:
            print("0 ",end="")
    print()


