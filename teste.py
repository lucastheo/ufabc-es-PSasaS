class Teste

    def __init__( self , lista_construcao: list , nome:str , detalhes:str , nMetodos:int ):
        self.lista_construcao = lista_construcao
        self.nome = nome
        self.detalhes = detalhes
        self.nMetodos = nMetodos
        self.id = None
        self.validado = False

    def criaModeloTeste(diagrama, requisitos):
        return "Modelagem Criada"

    #teste unitario

    def testeUnitario(codigo, modelo):
        if (!erro):
            return 1
        return 0

    def testeCompleto(lista_construcao):
        testes = []
        for i in range(nMetodos):
            testes.append(criaModeloTeste(diagrama, lista_todos_requisitos))
        for i in range(len(testes))
            if (! testeUnitario(codigo, testes[i])):
                print("\nMétodo com erro!!\n")
                print(nomeMetodo)
                return 0
        return 1
