import time
def criaModeloTeste(diagrama, requisitos):
    return "Modelagem Criada"

#teste unitario

def testeUnitario(codigo, modelo):
    erro = False
    if (!erro):
        return 1
    return 0

def testeCompleto(construcao, lista_todos_requisitos):
    print("\nCompilando código...")
    time.sleep(25)
    testes = []
    for i in range(nMetodos):
        testes.append(criaModeloTeste(diagrama, lista_todos_requisitos))
    for i in range(len(testes))
        if (! testeUnitario(codigo, testes[i])):
            print("\nMétodo com erro!!\n")
            print(nomeMetodo)
            return 0
    return 1
