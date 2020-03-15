
def gerar_requisitor():

    def get_key(val):
        for key, value in requisitos.items():
            if val == value:
                return key
            return "key doesn't exist"

    requisitos ={
        "Requisitos Funcionais:" : {

        },
        "Requisitos Não Funcionais:" : {

        },
        "Requisitos de Domínio:" : {

        },
        "Requisitos de Dados:" : {

        }
    }
    resposta = "n"
    tipo = "1"
    idReq = 1
    idAlter = 0

    while(resposta!="s"):
        tipo = input("\nDigite o código do tipo do requisito\nFuncional = 1\nNão Funcional = 2\nDomínio = 3\nDados = 4\n\n>>>Tipo desejado = ")
        if(tipo == "1"):
            requisitos["Requisitos Funcionais:"][str(idReq)]= input("\nDigite o nome do Requisito Funcional: >>>")
        elif (tipo == "2"):
            requisitos["Requisitos Não Funcionais:"][str(idReq)]=input("\nDigite o nome do Requisito Não Funcional: >>>")
        elif (tipo=="3"):
            requisitos["Requisitos de Domínio:"][str(idReq)]=input("\nDigite o nome do Requisito de Domínio: >>>")
        elif (tipo =="4"):
            requisitos["Requisitos de Dados:"][str(idReq)]=input("\nDigite o nome do Requisito de Dados: >>>")
        else:
            print("\nTipo Inválido!!\n")
        idReq = idReq +1
        resposta = input("Já adicionou todos os requisitos?(s/n)\n>>>")
    print(requisitos)
    resposta=input("\nRequisitos Válidos?(s/n):\n>>>")
    while(resposta!="s"):
        print(requisitos)
        tipo = input("\nQual requisito deseja Alterar?\n\nDigite o código do tipo do requisito\nFuncional = 1\nNão Funcional = 2\nDomínio = 3\nDados = 4\n>>>")
        if(tipo == "1"):
            print(requisitos["Requisitos Funcionais:"])
            idAlter = input("\nDigite o código do requisito para ser alterado\n>>>")
        elif (tipo == "2"):
            print(requisitos["Requisitos Não Funcionais:"])
            idAlter = input("\nDigite o código do requisito para ser alterado\n>>>")
        elif (tipo=="3"):
            print(requisitos["Requisitos de Domínio:"])
            idAlter = input("\nDigite o código do requisito para ser alterado\n>>>")
        elif (tipo =="4"):
            print(requisitos["Requisitos de Dados:"])
            idAlter = input("\nDigite o código do requisito para ser alterado\n>>>")
        else:
            print("\nTipo Inválido!!\n")
        if(idAlter!=0):
            if(tipo == "1"):
                requisitos["Requisitos Funcionais:"][str(idAlter)]= input("\nDigite o novo do Requisito Funcional: >>>")
            elif (tipo == "2"):
                requisitos["Requisitos Não Funcionais:"][str(idAlter)]=input("\nDigite o novo do Requisito Não Funcional: >>>")
            elif (tipo=="3"):
                requisitos["Requisitos de Domínio:"][str(idAlter)]=input("\nDigite o novo do Requisito de Domínio: >>>")
            elif (tipo =="4"):
                requisitos["Requisitos de Dados:"][str(idAlter)]=input("\nDigite o novo do Requisito de Dados: >>>")
            else:
                print("\nTipo Inválido!!\n")
            idReq = idReq +1
            print("\nRequisitos após alteração\n")
        print(requisitos)
        resposta=input("Requisitos Válidos?(s/n):\n>>>")
    return requisitos
