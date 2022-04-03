#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

class NoListaSequen:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor

class ListaSequen:
    def __init__(self, maximo, ultimo, dados):
        self.maximo = maximo
        self.ultimo = ultimo
        self.dados = dados

def listavazia(lista):
    for i in range(lista.maximo):
        no = NoListaSequen(None, None)
        lista.dados.append(no)

def visualizacao(lista):
    L = lista.dados
    print("Lista = (", end="")
    for i in range(lista.maximo):
        if i != (lista.maximo - 1):
            print("[ ", end="")
            print(L[i].valor, end="")
            print(" ], ", end = "")
        else:
            print("[ ", end="")
            print(L[i].valor, end="")
            print(" ])", end = "")

def buscarIndiceOrdenanda(x,lista):
    indice = 0
    n = lista.ultimo
    L = lista.dados
    i = 1
    while (i < n) and (L[i-1].chave < x):
        i = i + 1
    if L[i-1].chave == x:
        indice = i
    return indice

def buscar(x,lista):
    indice = buscarIndiceOrdenanda(x,lista)
    if indice > 0:
        return indice
    else:
        return None

def ordenarlista(lista):
    for j in range(1, lista.ultimo):
        chave = lista.dados[j]
        i = j - 1      
        while (i > 0) and (chave < lista.dados[i]):
            lista.dados[i+1] = lista.dados[i]
            i = i - 1
        lista.dados[i+1] = chave

def inserir(X,lista):
    n = lista.ultimo
    if n < lista.maximo:
        if buscarIndiceOrdenanda(X.chave, lista) == 0:
            n = n+1
            lista.dados[n] = X
            lista.ultimo = n
            if lista.ultimo > 1:
                ordenarlista(lista)
        else:
            print("Nó "+X.chave+" já existe!")
    else:
        print("Lista cheia!")

def remover(x, lista):
    n = lista.ultimo
    indice = buscarIndiceOrdenanda(x,lista)
    L = lista.dados
    if indice != 0:
        lista.dados[indice-1]= NoListaSequen(None, None)
        for i in range(indice-1, n):
            L[i] = L[i+1]
        lista.ultimo = n-1
        if lista.ultimo > 1:
                ordenarlista(lista)
        print("Nó " + x+ " foi removido")
    else:
        print("Nó "+x+" não existe")
    
    
m = int(input("Digite o valor M que representa o tamanho da lista:"))
lista = list()
novalista = ListaSequen(m,0,lista)
listavazia(novalista)

while True:
    escolha = input("Digite \"v\" para visualizar a lista, \"i\" para inserir na lista, \"r\" para remover na lista, \"b\" para buscar na lista ou \"0\" para sair: ")
    if escolha == "v":
        visualizacao(novalista)
        continue
    elif escolha == "i":
        chave = int(input("Digite uma chave para o novo nó a ser criado: "))
        valor = input("Digite uma informação para ser armazenado a este nó: ")
        no = NoListaSequen(chave, valor)
        inserir(no,novalista)
        continue
    elif escolha == "r":
        chave = int(input("Digite a chave do nó a ser removido: "))
        remover(chave, novalista)
        continue
    elif escolha == "b":
        chave = int(input("Digite a chave do nó a ser buscado: "))
        busca = buscar(chave,novalista)
        if busca == None:
            print("Nó não existe na lista")
        else:
            print("O nó "+chave+" se encontra no índice "+busca)
        continue
    elif escolha == 0:
        break
    else:
        continue