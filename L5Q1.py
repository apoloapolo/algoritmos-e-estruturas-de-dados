#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

trocas = 0
totalMH = 0

def criarlista(m):
    lista = list()
    for i in range(m):
        lista.append(None)
    return lista

def trocar(lista,a,b):
    global trocas
    trocas +=1
    c = lista[a]
    lista[a] = lista[b]
    lista[b] = c
    return lista

def retornarIndicePai(i):
    return i//2

def retornarIndiceFilhoEsquerda(i):
    return i*2

def retornarIndiceFilhoDireita(i):
    return i*2 + 1

def maxHeapfy(lista,i,m):
    global totalMH
    totalMH += 1
    l = retornarIndiceFilhoEsquerda(i)
    r = retornarIndiceFilhoDireita(i)
    if l <= m and (lista[l-1] > lista[i-1]):
        maior = l-1
    else:
        maior = i-1
    if r <= m and (lista[r-1] > lista[maior]):
        maior = r-1
    if maior != (i-1):
        lista = trocar(lista,i-1,maior)
        maxHeapfy(lista,maior+1,m)
        
def construirMaxHeap(lista,m):
    for i in range(m// 2 - 1, 0, -1):
        maxHeapfy(lista,i,m)
        print(f"\nLista Modificada (for do construirMaxHeap): {lista}\n")

def heapsort(lista,m):
    tamanho = m
    construirMaxHeap(lista,tamanho)
    for i in range(m,1,-1):
        lista = trocar(lista,0,i-1)
        tamanho-=1
        maxHeapfy(lista,1,tamanho)
        print(f"\nLista Modificada (for do heapsort): {lista}\n")
        
m = int(input("Digite o tamanho da lista a ser ordenada: "))
listaaserordenada = criarlista(m)
for i in range(m):
    listaaserordenada[i]=int(input(f"\nDigite o {i+1}º elemento da lista: "))
print(f"\nLista Original: {listaaserordenada}\n")
heapsort(listaaserordenada,m)
print(f"Total de trocas: {trocas}")
print(f"Total de maxHeapfy: {totalMH}")

