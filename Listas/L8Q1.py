#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

class No:
    def __init__(self,chave):
        self.chave = chave
        self.pai = None
        self.esquerda = None
        self.direita = None

class ArvoreBin:
    def __init__(self):
        self.raiz = None

    def inserir(self,x):
        X = No(x)
        pai = None
        pt = self.raiz
        while pt != None:
            pai = pt
            if X.chave <= pt.chave:
                pt = pt.esquerda
            else:
                pt = pt.direita
        X.pai = pai
        if pai == None:
            self.raiz = X
        elif X.chave <= pai.chave:
            pai.esquerda = X
        else:
            pai.direita = X

def preordem(pt):
    print(pt.chave, end= " ")
    if pt.esquerda != None:
        preordem(pt.esquerda)
    if pt.direita != None:
        preordem(pt.direita)

def ordem(pt):
    if pt.esquerda != None:
        ordem(pt.esquerda)
    print(pt.chave, end= " ")
    if pt.direita != None:
        ordem(pt.direita)

def posordem(pt):
    if pt.esquerda != None:
        posordem(pt.esquerda)
    if pt.direita != None:
        posordem(pt.direita)
    print(pt.chave, end= " ")

arvore = ArvoreBin()
raiz =  int(input())
arvore.raiz = No(raiz)
while True:
    valor =  int(input())
    if valor == 0:
        break
    arvore.inserir(valor)

print("Percurso em pré-ordem: ", end="") 
preordem(arvore.raiz)
print()
print("Percurso em ordem: ", end="")
ordem(arvore.raiz)
print()
print("Percurso em pós-ordem: ", end="")
posordem(arvore.raiz)