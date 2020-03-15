requisitos = []
reqFunc = ["Requisitos Funcionais:"]
reqNFunc = ["Requisitos Não Funcionais:"]
reqDom = ["Requisitos de Domínio"]
reqDados = ["Requisitos de Dados"]
resposta = "n"
tipo = "1"
while(resposta!="s"):
    tipo = input("\nDigite o código do tipo do requisito\nFuncional = 1\nNão Funcional = 2\nDomínio = 3\nDados = 4\n\nTipo desejado = ")
    if(tipo == "1"):
        reqFunc.append(input("\nDigite o nome do Requisito Funcional: "))
    elif (tipo == "2"):
        reqNFunc.append(input("\nDigite o nome do Requisito Não Funcional: "))
    elif (tipo=="3"):
        reqDom.append(input("\nDigite o nome do Requisito de Domínio: "))
    elif (tipo =="4"):
        reqDados.append(input("\nDigite o nome do Requisito de Dados: "))
    else:
        print("\nTipo Inválido!!\n")
    resposta = input("Já adicionou todos os requisitos?(s/n)\n")
