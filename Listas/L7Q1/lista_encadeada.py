#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

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
        
    def buscarle(self,x):
        pt = self.cabeca
        if pt != None:
            if self.tamanho == 1:
                if pt.chave == x:
                    return pt
                else:
                    return None
            elif self.tamanho == 2:
                contador = 0
                while contador < 2:
                    if pt.chave == x:
                        return pt
                    else:
                        pt = pt.proximo
                        contador+=1
                return None
            else:
                while pt.proximo != self.cabeca and pt.chave <= x:
                    if pt.chave == x:
                        return pt
                    else:
                        pt = pt.proximo
                if pt.chave == x:
                    return pt
                else:
                    return None
        else:
            print("Lista Vazia")
            
    def inserirle(self, X):
        if self.cabeca == None:
            X.proximo = X
            X.anterior = X
            self.cabeca = X
            self.tamanho+=1
        else:
            pt = self.buscarle(X.chave)
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

    def removerle(self,x):
        removido = self.buscarle(x)
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
                
    def imprimirle(self):
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