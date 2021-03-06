#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

import lista_encadeada as le

indice = 0

def criarlista(m):
    lista = list()
    for i in range(m):
        lista.append(None)
    return lista

class TabelaHash:
    def __init__(self, tamanho):
        self.tabela = criarlista(tamanho)
        self.tamanho = tamanho
        self.inseridos = 0
    
    def funcaohash(self, x):
        hash = x%self.tamanho
        return hash

    def inserir(self, x):
        global indice
        k = self.funcaohash(x)
        indice = k
        if self.inseridos < self.tamanho:
            if self.tabela[k] == None:
                no = le.No(x)
                self.tabela[k] = le.Lista()
                self.tabela[k].inserirle(no)
                self.inseridos += 1
            else:
                if k == self.tamanho - 1:
                    indice = 0
                else:
                    indice = self.funcaohash(k) + 1
                while indice != k:
                    if self.tabela[indice] == None:
                        no = le.No(x)
                        self.tabela[indice] = le.Lista()
                        self.tabela[indice].inserirle(no)
                        self.inseridos += 1
                        indice = k
                    else:
                        indice = self.funcaohash(indice) + 1
        else:
            no = le.No(x)
            self.tabela[k].inserirle(no)

    def buscar(self, x):
        global indice
        k = self.funcaohash(x)
        indice = k
        if self.inseridos < self.tamanho:
            pt = None
            if (self.tabela[k] != None) and (self.tabela[k].cabeca.chave == x):
                pt = self.tabela[k]
            else:
                if k == self.tamanho - 1:
                    indice = 0
                else:
                    indice =  self.funcaohash(k) + 1
                while indice != k:
                    if (self.tabela[k] != None) and (self.tabela[k].cabeca.chave == x):
                        pt = self.tabela[indice]
                        indice = k
                    else:
                        indice = self.funcaohash(indice) + 1
            return pt
        else:
            pt = None
            for i in range(self.tamanho):
                if pt != None:
                    break
                else:
                    for c in range(self.tabela[i].tamanho):
                        pt = self.tabela[i].buscarle(x)
                indice = i        
            return pt
    
    def remover(self, x):
        global indice
        pt = self.buscar(x)
        k = indice
        if self.inseridos < self.tamanho:
            if pt != None:
                self.tabela[k] = None
            else:
                print(f"N?? {x} n??o existe")
        else:
            if pt != None:
                self.tabela[k].removerle(x)
            else:
                print(f"N?? {x} n??o existe")
    
    def imprimir(self):
        for i in range(self.tamanho):
            if self.tabela[i] == None:
                print(f"??ndice {i}: Nulo (N??o h?? valores aqui)")
            elif self.tabela[i].tamanho == 1:
                print(f"??ndice {i}: {tabela.tabela[i].cabeca.chave}")
            else:
                print(f"??ndice {i}: ", end="")
                self.tabela[i].imprimirle()

tamanho =  int(input("Digite o tamanho da tabela hash a ser criada: "))
tabela = TabelaHash(tamanho)

while True:
    escolha = int(input("Digite a op????o desejada: 1. visualiza????o, 2. busca, 3.inser????o, 4. remo????o e 0. para sair: "))
    if escolha == 1:
        tabela.imprimir()
        continue
    elif escolha == 2:
        valor = int(input("Digite o valor a ser buscado: "))
        busca = tabela.buscar(valor)
        if busca == None:
            print("Valor n??o existe na lista")
        else:
            print(f"O valor {valor} est?? no ??ndice {indice} da tabela")
        continue
    elif escolha == 3:
        valor = int(input("Digite o valor a ser inserido: "))
        tabela.inserir(valor)
        continue
    elif escolha == 4:
        valor = int(input("Digite o valor a ser removido: "))
        tabela.remover(valor)
        continue
    elif escolha == 0:
        break