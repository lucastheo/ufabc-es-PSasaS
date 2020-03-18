import time
def criaModeloTeste( funcoes , requisitos):
    return executarTeste
#teste unitario
def executarTeste():
    return True 

def testeUnitario(lista_codigo, modelo):
    for codigo in lista_codigo:
        erro = False
        if (not erro):
            return 1
    return 0

def testeCompleto( objContrucao, lista_diagrama_Uml, lista_todos_requisitos):
    print("\nCompilando código...")
    time.sleep(5)
    testes = []
    
    for funcoes in objContrucao.lista_funcoes:
        testes.append(criaModeloTeste( funcoes , lista_todos_requisitos))
    
    for executarTeste in testes:
        if executarTeste() == False:
            return False

    return True
