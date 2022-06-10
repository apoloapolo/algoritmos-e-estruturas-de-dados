#Aluno: Vinicius Augusto Andrade Albuquerque (Apolo)

def criarlista(m):
    lista = list()
    for i in range(m):
        lista.append(None)
    return lista

def trocar(lista,a,b):
    c = lista[a]
    lista[a] = lista[b]
    lista[b] = c
    return lista

def quicksort(lista, p, r):
    if p < r:
        q = particionar(lista, p, r)
        quicksort(lista, p, q-1)
        quicksort(lista, q + 1, r)

def particionar(lista, p, r):
    pivo = lista[r].iniciativa
    i = p
    for j in range(p,r):
        if lista[j].iniciativa >= pivo:
            lista = trocar(lista,j,i)
            i+=1
    lista = trocar(lista,i,r)
    return i

class lutador:
    def __init__(self, id, dano, vida, iniciativa):
        self.id = id
        self.dano = dano
        self.vida = vida
        self.iniciativa = iniciativa
        self.jalutou = False
    def resetarjalutou(self):
        self.jalutou = False

def inserirlutador(time, lutador):
    global qtdTime1
    global qtdTime2
    global time1
    global time2
    if time == 1:
        qtdTime1 += 1
        lista = criarlista(qtdTime1)
        for i in range(qtdTime1-1):
            lista[i] = time1[i]
        lista[qtdTime1-1] = lutador
        time1 = lista
    else:
        qtdTime2 += 1
        lista = criarlista(qtdTime2)
        for i in range(qtdTime2-1):
            lista[i] = time2[i]
        lista[qtdTime2-1] = lutador
        time2 = lista

def inserircemiterio(time, lutador):
    global qtdCemiterio1
    global qtdCemiterio2
    global cemiterio1
    global cemiterio2
    if time == 1:
        qtdCemiterio1 += 1
        lista = criarlista(qtdCemiterio1)
        for i in range(qtdCemiterio1-1):
            lista[i] = cemiterio1[i]
        lista[qtdCemiterio1-1] = lutador
        cemiterio1 = lista
        quicksort(cemiterio1, 0, qtdCemiterio1-1)
    else:
        qtdCemiterio2 += 1
        lista = criarlista(qtdCemiterio2)
        for i in range(qtdCemiterio2-1):
            lista[i] = cemiterio2[i]
        lista[qtdCemiterio2-1] = lutador
        cemiterio2 = lista
        quicksort(cemiterio2, 0, qtdCemiterio2-1)

def buscarlutador(id):
    global time1
    global time2
    global timebusca
    l = None
    for lutador in time1:
        if lutador.id == id:
            timebusca = 1
            l = lutador
            return l
    for lutador in time2:
        if lutador.id == id:
            timebusca = 2
            l = lutador
            return l
    return l

def removerlutador(time, lutador):
    global qtdTime1
    global qtdTime2
    global time1
    global time2
    if time == 1:
        qtdTime1 -= 1
        lista = criarlista(qtdTime1)
        valor = 0
        for i in range(qtdTime1+1):
            if time1[i] == lutador:
                valor = i
                break
            else:
                lista[i] = time1[i]
        while valor < qtdTime1:
            lista[valor] = time1[valor+1]
            valor += 1
        time1 = lista
    else:
        qtdTime2 -= 1
        lista = criarlista(qtdTime2)
        valor = 0
        for i in range(qtdTime2+1):
            if time2[i] == lutador:
                valor = i
                break
            else:
                lista[i] = time2[i]
        while valor < qtdTime2:
            lista[valor] = time2[valor+1]
            valor += 1 
        time2 = lista

def luta():
    global qtdTime1
    global qtdTime2
    global time1
    global time2
    while True:
        if qtdTime1 <= 0 or qtdTime2 <= 0:
            break
        else:
            if qtdTime1 >= qtdTime2:
                while time1[0].jalutou == False:
                    time1[0].vida -= time2[0].dano
                    time2[0].vida -= time1[0].dano
                    time1[0].jalutou = True
                    time2[0].jalutou = True
                    if time1[0].vida <= 0 and time2[0].vida > 0:
                        l = time1[0]
                        removerlutador(1, time1[0])
                        inserircemiterio(1, l)
                        l = time2[0]
                        removerlutador(2, time2[0])
                        inserirlutador(2, l)
                        if qtdTime1 <= 0 or qtdTime2 <= 0:
                            break
                        continue
                    elif time1[0].vida > 0 and time2[0].vida <= 0:
                        l = time2[0]
                        removerlutador(2, time2[0])
                        inserircemiterio(2, l)
                        l = time1[0]
                        removerlutador(1, time1[0])
                        inserirlutador(1, l)
                        if qtdTime1 <= 0 or qtdTime2 <= 0:
                            break
                        continue
                    elif time1[0].vida <= 0 and time2[0].vida <= 0:
                        l = time1[0]
                        removerlutador(1, time1[0])
                        inserircemiterio(1, l)
                        l = time2[0]
                        removerlutador(2, time2[0])
                        inserircemiterio(2, l)
                        if qtdTime1 <= 0 or qtdTime2 <= 0:
                            break
                        continue
                    elif time1[0].vida > 0 and time2[0].vida > 0:
                        l = time2[0]
                        removerlutador(2, time2[0])
                        inserirlutador(2, l)
                        l = time1[0]
                        removerlutador(1, time1[0])
                        inserirlutador(1, l)
                        if qtdTime1 <= 0 or qtdTime2 <= 0:
                            break
                        continue
                break
            else:
                while time2[0].jalutou == False:
                    time1[0].vida -= time2[0].dano
                    time2[0].vida -= time1[0].dano
                    time1[0].jalutou = True
                    time2[0].jalutou = True
                    if time1[0].vida <= 0 and time2[0].vida > 0:
                        l = time1[0]
                        removerlutador(1, time1[0])
                        inserircemiterio(1, l)
                        l = time2[0]
                        removerlutador(2, time2[0])
                        inserirlutador(2, l)
                        if qtdTime1 <= 0 or qtdTime2 <= 0:
                            break
                        continue
                    elif time1[0].vida > 0 and time2[0].vida <= 0:
                        l = time2[0]
                        removerlutador(2, time2[0])
                        inserircemiterio(2, l)
                        l = time1[0]
                        removerlutador(1, time1[0])
                        inserirlutador(1, l)
                        if qtdTime1 <= 0 or qtdTime2 <= 0:
                            break
                        continue
                    elif time1[0].vida <= 0 and time2[0].vida <= 0:
                        l = time1[0]
                        removerlutador(1, time1[0])
                        inserircemiterio(1, l)
                        l = time2[0]
                        removerlutador(2, time2[0])
                        inserircemiterio(2, l)
                        if qtdTime1 <= 0 or qtdTime2 <= 0:
                            break
                        continue
                    elif time1[0].vida > 0 and time2[0].vida > 0:
                        l = time2[0]
                        removerlutador(2, time2[0])
                        inserirlutador(2, l)
                        l = time1[0]
                        removerlutador(1, time1[0])
                        inserirlutador(1, l)
                        if qtdTime1 <= 0 or qtdTime2 <= 0:
                            break
                        continue
                break
    for jogador in time1:
        jogador.resetarjalutou()
    for jogador in time2:
        jogador.resetarjalutou()
    return
        
time1 = criarlista(0)
time2 = criarlista(0)
cemiterio1 = criarlista(0)
cemiterio2 = criarlista(0)

qtdTime1 = 0
qtdTime2 = 0
qtdCemiterio1 = 0
qtdCemiterio2 = 0

timebusca = None

print("-----COMBATE-----")
while True:
    print()
    escolha = int(input("Digite a opção desejada: 1. inserção de lutadores, 2. relatório de status, 3. fuga de lutador, 4. iniciar luta: "))
    if escolha == 1:
        print()
        time = int(input("Digite a opção desejada: 1. inserção no time 1, 2. inserção no time 2: "))
        while True:
            achou = False
            print()
            id = input("Digite o ID do lutador: ")
            for jogador in time1:
                if jogador.id == id:
                    print("Esse ID já está cadastrado, digite outro.")
                    achou = True
            for jogador in time2:
                if jogador.id == id:
                    print("Esse ID já está cadastrado, digite outro.")
                    achou = True
            for jogador in cemiterio1:
                if jogador.id == id:
                    print("Esse ID já está cadastrado, digite outro.")
                    achou = True
            for jogador in cemiterio2:
                if jogador.id == id:
                    print("Esse ID já está cadastrado, digite outro.")
                    achou = True
            if achou:
                continue
            else:
                break
        dano = int(input("Digite o dano do lutador: "))
        vida = int(input("Digite a vida do lutador: "))
        while True:
            inciativa = int(input("Digite a iniciativa do lutador: "))
            if inciativa > 100 or inciativa < 1:
                print("Digite um valor entre 1 e 100")
                continue
            else:
                break
        l = lutador(id, dano, vida, inciativa)
        inserirlutador(time, l)
        if time == 1:
            quicksort(time1, 0, qtdTime1-1)
        else:
            quicksort(time2, 0, qtdTime2-1)
        continue
    elif escolha == 2:
        print()
        time = int(input("Digite a opção desejada: 1. relatório do time 1, 2. relatório do time 2: "))
        print()
        if time == 1:
            print("VIVOS:")
            if qtdTime1 == 0:
                print("Vazio")
                print()
            else:
                print("ID | Iniciativa | Vida")
                for jogador in time1:
                    print(f"{jogador.id} | {jogador.iniciativa} | {jogador.vida}")
                print()
            print("MORTOS:")
            if qtdCemiterio1 == 0:
                print("Vazio")
            else:
                print("ID | Iniciativa | Vida")
                for jogador in cemiterio1:
                    print(f"{jogador.id} | {jogador.iniciativa} | {jogador.vida}")
            continue
        else:
            print("VIVOS:")
            if qtdTime2 == 0:
                print("Vazio")
                print()
            else:
                print("ID | Iniciativa | Vida")
                for jogador in time2:
                    print(f"{jogador.id} | {jogador.iniciativa} | {jogador.vida}")
                print()
            print("MORTOS:")
            if qtdCemiterio2 == 0:
                print("Vazio")
            else:
                print("ID | Iniciativa | Vida")
                for jogador in cemiterio2:
                    print(f"{jogador.id} | {jogador.iniciativa} | {jogador.vida}")
            continue
    elif escolha == 3:
        print()
        id = input("Digite o ID do lutador a fugir: ")
        l = buscarlutador(id)
        if l:
            removerlutador(timebusca, l)
            print(f"O lutador com ID {id} fugiu!")
        else:
            print("O lutador não existe ou está morto")
        continue
    elif escolha == 4:
        print()
        termino = False
        while termino == False:
            luta()
            if qtdTime1 > 0 and qtdTime2 <= 0:
                print(f"""O time 1 venceu!
Score time 1: {qtdCemiterio2}
Score time 2: {qtdCemiterio1}""")
                termino = True
            elif qtdTime1 <= 0 and qtdTime2 > 0:
                print(f"""O time 2 venceu!
Score time 1: {qtdCemiterio2}
Score time 2: {qtdCemiterio1}""")
                termino = True
            elif qtdCemiterio1 >= 20 and qtdCemiterio2 < 20:
                print(f"""O time 2 venceu!
Score time 1: {qtdCemiterio2}
Score time 2: {qtdCemiterio1}""")
                termino = True
            elif qtdCemiterio2 >= 20 and qtdCemiterio1 < 20:
                print(f"""O time 1 venceu!
Score time 1: {qtdCemiterio2}
Score time 2: {qtdCemiterio1}""")
                termino = True
            elif (qtdCemiterio2 >= 20 and qtdCemiterio1 >= 20) or (qtdTime2 <= 0 and qtdTime1 <= 0):
                if qtdCemiterio2 == qtdCemiterio1:
                    print(f"""Empate!
Score time 1: {qtdCemiterio2}
Score time 2: {qtdCemiterio1}""")
                    termino = True
                elif qtdCemiterio2 > qtdCemiterio1:
                    print(f"""O time 1 venceu!
Score time 1: {qtdCemiterio2}
Score time 2: {qtdCemiterio1}""")
                    termino = True
                elif qtdCemiterio2 < qtdCemiterio1:
                    print(f"""O time 2 venceu!
Score time 1: {qtdCemiterio2}
Score time 2: {qtdCemiterio1}""")
                    termino = True
            else:
                break
        if termino:
            print()
            print("-----FIM DE JOGO----")
            break
        else:
            print("-----NOVO TURNO-----")
            continue