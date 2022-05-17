#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

class NoArvore:
    def __init__(self,chave):
        self.chave = chave
        self.pai = None
        self.rank = 0

def make_set_rank(x):
    no = NoArvore(x)
    no.pai = no
    return no

def find_set_compressao(x):
    if x.chave != x.pai.chave:
        x.pai = find_set_compressao(x.pai)
    return x.pai

def union_rank(x,y):
    xrepre = find_set_compressao(x)
    yrepre = find_set_compressao(y)
    if xrepre == yrepre:
        print("Os nós já estão no mesmo conjunto")
    else:
        link(xrepre, yrepre)
    
def link(x,y):
    if x.rank > y.rank:
        y.pai = x
    elif x.rank < y.rank:
        x.pai = y
    else:
        x.rank += 1