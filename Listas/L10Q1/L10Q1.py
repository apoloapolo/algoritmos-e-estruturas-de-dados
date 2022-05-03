#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)


no_responsavel = None
rd = False
re = False
rdd = False
red = False

class No:
    def __init__(self,chave):
        self.chave = chave
        self.altura = 1
        self.esquerda = None
        self.direita = None
        self.fatorBalanceamento = 0
    
class ArvoreAVL:
    def __init__(self):
        self.raiz = None
        self.altura = 1
    
    def inserir(self, pt, x):
        global no_responsavel
        global rd
        global re
        global rdd
        global red
        if not pt:
            return No(x)
        elif x <= pt.chave:
            pt.esquerda = self.inserir(pt.esquerda, x)
        else:
            pt.direita = self.inserir(pt.direita, x)
        pt.altura = 1 + max(self.getAltura(pt.esquerda), self.getAltura(pt.direita))
        balanceamento = self.getBalanceamento(pt)
        pt.fatorBalanceamento = balanceamento
        if balanceamento < -1 and x < pt.esquerda.chave:
            rd = True
            no_responsavel = pt.chave
            return self.rotacaoDireita(pt)
        elif balanceamento > 1 and x > pt.direita.chave:
            re = True
            no_responsavel = pt.chave
            return self.rotacaoEsquerda(pt)
        elif balanceamento < -1 and x > pt.esquerda.chave:
            rdd = True
            no_responsavel = pt.chave
            pt.esquerda = self.rotacaoEsquerda(pt.esquerda)
            return self.rotacaoDireita(pt)
        elif balanceamento > 1 and x < pt.direita.chave:
            red = True
            no_responsavel = pt.chave
            pt.direita = self.rotacaoDireita(pt.direita)
            return self.rotacaoEsquerda(pt)
        self.raiz = pt
        self.altura = pt.altura
        return pt
 
    def rotacaoEsquerda(self, p):
        u = p.direita
        v = u.esquerda
        u.esquerda = p
        p.direita = v
        p.altura = 1 + max(self.getAltura(p.esquerda), self.getAltura(p.direita))
        u.altura = 1 + max(self.getAltura(u.esquerda), self.getAltura(u.direita))
        return u
 
    def rotacaoDireita(self, p):
        u = p.esquerda
        v = u.direita
        u.direita = p
        p.esquerda = v
        p.altura = 1 + max(self.getAltura(p.esquerda), self.getAltura(p.direita))
        u.altura = 1 + max(self.getAltura(u.esquerda), self.getAltura(u.direita))
        return u
 
    def getAltura(self, pt):
        if not pt:
            return 0
        return pt.altura
 
    def getBalanceamento(self, pt):
        if not pt:
            return 0
        return self.getAltura(pt.direita) - self.getAltura(pt.esquerda)

    def definirFatorBalanceamento(self, pt):
        pt.fatorBalanceamento = self.getBalanceamento(pt)
        if pt.esquerda != None:
            self.definirFatorBalanceamento(pt.esquerda)
        if pt.direita != None:
            self.definirFatorBalanceamento(pt.direita)

    def ordem(self, pt):
        if pt.esquerda != None:
            self.ordem(pt.esquerda)
        if pt.fatorBalanceamento > 0:
            print(f"{pt.chave}(+{pt.fatorBalanceamento})"  , end= " ")
        else:
            print(f"{pt.chave}({pt.fatorBalanceamento})"  , end= " ")
        if pt.direita != None:
            self.ordem(pt.direita)

# 45 30 18 60 81 36 101 5 8 3
arquivo = open(, 'r')
for linha in arquivo:
    print(linha)

arvore = ArvoreAVL()
raiz = None
lista = [17, 90, 87, 30, 23, 6, 84, 60, 3]

"""for i in lista:
    no_responsavel = None
    rd = False
    re = False
    rdd = False
    red = False
    raiz = arvore.inserir(raiz, i)
    if not no_responsavel:
        print("arvore ja balanceada.")
        arvore.definirFatorBalanceamento(raiz)
        arvore.ordem(raiz)
        print()
        print(f"{arvore.altura}")
    else:
        if rd:
            print(f"no responsavel: {no_responsavel}")
            arvore.ordem(raiz)
            print()
            print("rotacao direita.")
            arvore.definirFatorBalanceamento(raiz)
            arvore.ordem(raiz)
            print()
            print(f"{arvore.altura}")
        elif re:
            print(f"no responsavel: {no_responsavel}")
            arvore.ordem(raiz)
            print()
            print("rotacao esquerda.")
            arvore.definirFatorBalanceamento(raiz)
            arvore.ordem(raiz)
            print()
            print(f"{arvore.altura}")
        elif rdd:
            print(f"no responsavel: {no_responsavel}")
            arvore.ordem(raiz)
            print()
            print("rotacao direita dupla.")
            arvore.definirFatorBalanceamento(raiz)
            arvore.ordem(raiz)
            print()
            print(f"{arvore.altura}")
        elif red:
            print(f"no responsavel: {no_responsavel}")
            arvore.ordem(raiz)
            print()
            print("rotacao esquerda dupla.")
            arvore.definirFatorBalanceamento(raiz)
            arvore.ordem(raiz)
            print()
            print(f"{arvore.altura}")"""