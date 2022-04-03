#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

trocas = 0

def criarlista(m):
    lista = list()
    for i in range(m):
        lista.append(None)
    return lista

def trocar(lista,a,b):
    c = lista[a]
    lista[a] = lista[b]
    lista[b] = c
    global trocas
    trocas +=1
    return lista

def quicksort(lista, p, r):
    if p < r:
        q = particionar(lista, p, r)
        quicksort(lista, p, q-1)
        quicksort(lista, q + 1, r)

def particionar(lista, p, r):
    pivo = lista[r]
    i = p
    for j in range(p,r):
        if lista[j] <= pivo:
            lista = trocar(lista,j,i)
            i+=1
    lista = trocar(lista,i,r)
    print(f"\nLista Modificada: {lista}\n")
    return i

m = int(input("Digite o tamanho da lista a ser ordenada: "))
listaaserordenada = criarlista(m)
for i in range(m):
    listaaserordenada[i]=int(input(f"\nDigite o {i+1}º elemento da lista: "))
print(f"\nLista Original: {listaaserordenada}\n")
quicksort(listaaserordenada,0,m-1)
print(f"Total de trocas: {trocas}")
