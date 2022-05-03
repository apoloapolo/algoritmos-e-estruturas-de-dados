#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

no_responsavel = None
rd = False
re = False
rdd = False
red = False
string_ordem = ""

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
        global string_ordem
        if pt.esquerda != None:
            self.ordem(pt.esquerda)
        if pt.fatorBalanceamento > 0:
            string_ordem += str(pt.chave)+"("+"+"+str(pt.fatorBalanceamento)+")"
            string_ordem += " "
        else:
            string_ordem += str(pt.chave)+"("+str(pt.fatorBalanceamento)+")"
            string_ordem += " "
        if pt.direita != None:
            self.ordem(pt.direita)

def resetarStringOrdem():
    global string_ordem
    string_ordem = ""

entrada = open('L10Q1_in.txt', 'r')
lista_arvores = []
for linha in entrada:
    lista_arvores.append(linha.split())
print(lista_arvores)
entrada.close
saida = open('L10Q1_out.txt', 'w')
saida.close

for a in lista_arvores:
    arvore = ArvoreAVL()
    raiz = None
    resetarStringOrdem()
    for i in a:
        no_responsavel = None
        rd = False
        re = False
        rdd = False
        red = False
        saida = open('L10Q1_out.txt', 'a')
        raiz = arvore.inserir(raiz, int(i))
        if not no_responsavel:
            saida.write("arvore ja balanceada.\n")
            arvore.definirFatorBalanceamento(raiz)
            arvore.ordem(raiz)
            saida.write(string_ordem + "\n")
            resetarStringOrdem()
            saida.write(str(arvore.altura) + "\n")
            saida.close
        else:
            if rd:
                saida.write("no responsavel: " + str(no_responsavel) + "\n")
                arvore.ordem(raiz)
                saida.write(string_ordem + "\n")
                resetarStringOrdem()
                saida.write("rotacao direita.\n")
                arvore.definirFatorBalanceamento(raiz)
                arvore.ordem(raiz)
                saida.write(string_ordem + "\n")
                resetarStringOrdem()
                saida.write(str(arvore.altura) + "\n")
                saida.close
            elif re:
                saida.write("no responsavel: " + str(no_responsavel) + "\n")
                arvore.ordem(raiz)
                saida.write(string_ordem + "\n")
                resetarStringOrdem()
                saida.write("rotacao esquerda.\n")
                arvore.definirFatorBalanceamento(raiz)
                arvore.ordem(raiz)
                saida.write(string_ordem + "\n")
                resetarStringOrdem()
                saida.write(str(arvore.altura) + "\n")
                saida.close
            elif rdd:
                saida.write("no responsavel: " + str(no_responsavel) + "\n")
                arvore.ordem(raiz)
                saida.write(string_ordem + "\n")
                resetarStringOrdem()
                saida.write("rotacao direita dupla.\n")
                arvore.definirFatorBalanceamento(raiz)
                arvore.ordem(raiz)
                saida.write(string_ordem + "\n")
                resetarStringOrdem()
                saida.write(str(arvore.altura) + "\n")
                saida.close
            elif red:
                saida.write("no responsavel: " + str(no_responsavel) + "\n")
                arvore.ordem(raiz)
                saida.write(string_ordem + "\n")
                resetarStringOrdem()
                saida.write("rotacao esquerda dupla.\n")
                arvore.definirFatorBalanceamento(raiz)
                arvore.ordem(raiz)
                saida.write(string_ordem + "\n")
                resetarStringOrdem()
                saida.write(str(arvore.altura) + "\n")
                saida.close
    saida = open('L10Q1_out.txt', 'a')     
    saida.write("\n")
    saida.close
saida = open('L10Q1_out.txt', 'a')     
saida.write("\n")
saida.close