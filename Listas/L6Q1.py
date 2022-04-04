#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

indice = 0

class No:
    def __init__(self, chave):
        self.chave = chave
        self.anterior = None
        self.proximo = None
    def get_chave(self):
        return self.chave 
    
class Lista:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
        
    def buscar(self,x):
        global indice
        pt = self.cabeca
        if pt != None:
            if self.tamanho == 1:
                if pt.chave == x:
                    return pt
                else:
                    indice+=1
                    return None
            elif self.tamanho == 2:
                contador = 0
                while contador < 2:
                    if pt.chave == x:
                        return pt
                    else:
                        indice+=1
                        pt = pt.proximo
                        contador+=1
                return None
            else:
                while pt.proximo != self.cabeca and pt.chave <= x:
                    if pt.chave == x:
                        return pt
                    else:
                        indice+=1
                        pt = pt.proximo
                if pt.chave == x:
                    return pt
                else:
                    return None
        else:
            print("Lista Vazia")
            
    def inserir(self, X):
        if self.cabeca == None:
            X.proximo = X
            X.anterior = X
            self.cabeca = X
            self.tamanho+=1
        else:
            pt = self.buscar(X.chave)
            if pt == None:
                atual = self.cabeca
                if atual.proximo == self.cabeca:
                    if atual.chave < X.chave:
                        atual.proximo = X
                        X.anterior = atual
                        X.proximo = self.cabeca
                        self.cabeca.anterior = X
                        self.tamanho+=1
                    else:
                        X.anterior = atual
                        X.proximo = atual
                        self.cabeca = X
                        atual.anterior = self.cabeca
                        atual.proximo = X
                        self.tamanho+=1
                else:
                    contador = 0
                    while atual.chave < X.chave and atual.proximo != self.cabeca:
                        atual = atual.proximo
                        contador+=1
                    if contador == 0:
                        X.proximo = atual
                        X.anterior = atual.anterior
                        self.cabeca = X
                        atual.anterior = X
                        X.anterior.proximo = X
                        self.tamanho+=1
                    elif contador == self.tamanho - 1 and X.chave > atual.chave:
                        X.anterior = atual
                        X.proximo = self.cabeca
                        self.cabeca.anterior = X
                        atual.proximo = X
                        self.tamanho+=1
                    else:
                        X.proximo = atual
                        X.anterior = atual.anterior
                        X.anterior.proximo = X
                        atual.anterior = X
                        self.tamanho+=1
            else:
                print("Valor já existe na lista, não pode ser adicionado.")

    def remover(self,x):
        removido = self.buscar(x)
        if removido == None:
            print("Valor não pode ser removido pois não existe na lista")
        else:
            if self.tamanho > 1 and removido == self.cabeca:
                self.cabeca.proximo.anterior = self.cabeca.anterior
                self.cabeca = self.cabeca.proximo
                self.tamanho-=1
            elif self.tamanho > 1 and removido.proximo != self.cabeca:
                removido.anterior.proximo = removido.proximo
                removido.proximo.anterior = removido.anterior
                self.tamanho-=1
            elif self.tamanho > 1 and removido.proximo == self.cabeca:
                removido.anterior.proximo = self.cabeca
                self.cabeca.anterior = removido.anterior
                self.tamanho-=1
            else:
                self.cabeca = None
                self.tamanho = 0
                
    def imprimir(self):
        if self.tamanho == 0:
            print("Lista Vazia!")
        elif self.tamanho == 1:
            print("[", end="")
            print(self.cabeca.chave, end="")
            print("]")
        else:
            atual = self.cabeca
            contador = 0
            print("[ ", end="")
            while contador < self.tamanho-1:
                print(atual.chave, end="")
                print(", ", end="")
                atual = atual.proximo
                contador+=1
            print(f"{atual.chave} ]")    

    def imp_rev(self):
        if self.tamanho == 0:
            print("Lista Vazia!")
        elif self.tamanho == 1:
            print("[", end="")
            print(self.cabeca.chave, end="")
            print("]")
        else:
            atual = self.cabeca
            contador = 0
            print("[ ", end="")
            while contador < self.tamanho -1:
                print(atual.anterior.chave, end="")
                print(", ", end="")
                atual = atual.anterior
                contador+=1
            print(f"{atual.anterior.chave} ]")
            
lista = Lista()
while True:
    indice = 0
    escolha = int(input("Digite a opção desejada: 1. visualização crescente, 2. visualização decrescente, 3. busca, 4.inserção, 5. remoção e 0. para sair: "))
    if escolha == 1:
        lista.imprimir()
        continue
    elif escolha == 2:
        lista.imp_rev()
        continue
    elif escolha == 3:
        valor = int(input("Digite o valor a ser buscado: "))
        busca = lista.buscar(valor)
        if busca == None:
            print("Valor não existe na lista")
        else:
            print(f"O valor {valor} está na {indice+1}ª posição da lista")
        continue
    elif escolha == 4:
        valor = int(input("Digite o valor a ser inserido: "))
        no = No(valor)
        lista.inserir(no)
        continue
    elif escolha == 5:
        valor = int(input("Digite o valor a ser removido: "))
        lista.remover(valor)
        continue
    elif escolha == 0:
        break
