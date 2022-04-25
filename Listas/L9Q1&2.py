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

    def buscar(self, x, pt):
        if (pt == None) or (pt.chave == x):
            return pt
        elif x < pt.chave:
            return self.buscar(x, pt.esquerda)
        else:
            return self.buscar(x, pt.direita)

    def encontrarMin(self, pt):
        while pt.esquerda != None:
            pt = pt.esquerda
        return pt
    
    def encontrarMax(self, pt):
        while pt.direita != None:
            pt = pt.direita
        return pt

    def sucessor(self, pt):
        if pt.direita != None:
            return self.encontrarMin(pt.direita)
        else:
            pai = pt.pai
            while (pai != None) and (pt.chave == pai.direita.chave):
                pt = pai
                pai = pai.pai
            return pai
    
    def remover(self, x):
        pt = self.buscar(x, self.raiz)
        if pt == None:
            print(f"Nó {x} não existe!")
        else:
            if (pt.esquerda == None) and (pt.direita == None):
                self.removerSemFilhos(pt)
            elif (pt.esquerda != None) and (pt.direita != None):
                self.removerDoisFilhos(pt)
            else:
                self.removerUnicoFilho(pt)
        return pt

    def removerSemFilhos(self, pt):
        pai = pt.pai
        if pai != None:
            if pai.chave >= pt.chave:
                pai.esquerda = None
            else:
                pai.direita = None
        else:
            self.raiz = None
        pt.pai = None
    
    def removerUnicoFilho(self, pt):
        pai = pt.pai
        filho = None
        if pt.esquerda != None:
            filho = pt.esquerda
            pt.esquerda = None
        else:
            filho = pt.direita
            pt.direita = None
        if pai != None:
            filho.pai = pai
            if filho.chave <= pai.chave:
                pai.esquerda = filho
            else:
                pai.direita = filho
        else:
            self.raiz = filho
        pt.pai = None

    def removerDoisFilhos(self, pt):
        sucessor = self.sucessor(pt)
        sucessor = self.remover(sucessor.chave)
        sucessor.pai = pt.pai
        pt.pai = None
        sucessor.esquerda = pt.esquerda
        pt.esquerda = None
        sucessor.direita = pt.direita
        pt.direita = None
        pai = sucessor.pai
        if pai != None:
            if pai.chave >= sucessor.chave:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor
        else:
            self.raiz = sucessor
        sucessor.esquerda.pai = sucessor
        if sucessor.direita != None:
            sucessor.direita.pai = sucessor

def ordem(pt):
    if pt.esquerda != None:
        ordem(pt.esquerda)
    print(pt.chave, end= " ")
    if pt.direita != None:
        ordem(pt.direita)

arvore = ArvoreBin()
raiz =  int(input("Valor da raiz: "))
arvore.raiz = No(raiz)
while True:
    opcao =  int(input("Opção desejada: "))
    if opcao == 0:
        break
    elif opcao == 1:
        valor = int(input("Digite o valor a ser inserido: "))
        arvore.inserir(valor)
        print("Percurso em ordem: ", end="")
        ordem(arvore.raiz)
        print()
        continue
    elif opcao == 2:
        valor = int(input("Digite o valor a ser removido: "))
        remo = arvore.remover(valor)
        if remo:
            print(f"O valor {remo.chave} foi removido da árvore")
        print("Percurso em ordem: ", end="")
        ordem(arvore.raiz)
        print()
        continue
    elif opcao == 3:
        valor = int(input("Digite o valor a ser buscado: "))
        vb = arvore.buscar(valor,arvore.raiz)
        if vb:
            print(f"O valor {vb.chave} foi encontrado na árvore!")
            print()
        else:
            print(f"O valor {valor} NÃO foi encontrado na árvore!")
            print()
        continue
    elif opcao == 4:
        valor = int(input("Digite um valor para buscar o sucessor: "))
        vb = arvore.buscar(valor, arvore.raiz)
        if vb:
            suc = arvore.sucessor(vb)
            if suc:
                print(f"O sucessor de {vb.chave} é {suc.chave}")
                print()
            else:
                print(f"Não há sucessor de {vb.chave} pois ele é o maior valor da lista")
                print()
        else:
            print(f"O valor {valor} NÃO foi encontrado na árvore!")
            print()
        continue