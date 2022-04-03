#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

def criarlista(m):
    lista = list()
    for i in range(m):
        lista.append(None)
    return lista


def mergesort(lista, p, r):
    
    if p < r:
        q = (p + r)//2
        mergesort(lista, p, q)
        mergesort(lista, q+1, r)
        print(f"\n\nLista original: {lista}")
        merge(lista, p, q, r)

        
def merge(lista, p, q, r):
    tamanho  = r-p+1
    n1 = p
    n2 = q+1
    fim_n1 = 0
    fim_n2 = 0
    arranjo = criarlista(tamanho)
    for i in range(tamanho):
        if fim_n1 == 0  and fim_n2 == 0:
            if lista[n1] < lista[n2]:
                arranjo[i] = lista[n1]
                n1 += 1
                if n1 > q:
                    fim_n1 = 1
            else:
                arranjo[i] = lista[n2]
                n2 += 1
                if n2 > r:
                    fim_n2 = 1
        else:
            if fim_n1 == 0:
                arranjo[i] = lista[n1]
                n1 += 1
            else:
                arranjo[i] = lista[n2]
                n2 += 1
    for i in range(tamanho):
        lista[p] = arranjo[i]
        p += 1
    print(f"\nLista modificada: {lista}\n")    


m = int(input("Digite o tamanho da lista a ser ordenada: "))
listaaserordenada = criarlista(m)
for i in range(m):
    listaaserordenada[i]=int(input(f"\nDigite o {i+1}º elemento da lista: "))
mergesort(listaaserordenada,0,m-1)



