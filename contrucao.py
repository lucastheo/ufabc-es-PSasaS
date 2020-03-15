class Contrucao:
    def __init__(self ):
        self.lista_classe = list()
        self.lista_funcoes = list()
        self.lista_codigo = list()
        self.lista_diagrama_Ml = list()

    def __iter__( self ):
        return self

    def __next__( self ):
        print("<<<Possiveis tipos de entrada")
        print("\tCodigo 1")
        print("\tFuncao/Metodo 2")
        print("\tClasse 3")
        print("\tDiagrama ML 4")

        entrada = input("\n>>>Qual tipo de entrada? ")

        if entrada.startswith('1'):
            codigo = input(">>>Entre com o codigo: ")
            self.lista_codigo.append( codigo )
        elif entrada.startswith('2'):
            funcao = Funcao()
            self.lista_funcoes.append( funcao )
            self.lista_codigo.append( funcao.codigo )
        elif entrada.startswith('3'):
            classe = Classe()
            self.lista_classe.append( classe )
            for funcao in classe.lista_funcoes:
                self.lista_funcoes.append( funcao )
                self.lista_codigo.append( funcao.codigo )
        elif entrada.startswith('4'):
            diagrama_ml = DiagramaMl()
            self.lista_diagrama_Ml.append( diagrama_ml )
            

class Classe:
    def __init__( self ):
        self.lista_funcoes = list()
        self.lista_codigo = list()
        flag = True        
        while flag:
            print(">>>Entradas possiveis para a classe")
            print("\tCodigo 1")
            print("\tFuncao 2")
            print("\tParar  3")
            entrada = input(">>>Qual tipo da entrada? ")
            
            if entrada.startswith("1"):
                codigo = input(">>>Entre com o código: ")
                self.lista_codigo.append( codigo )
            elif entrada.startswith("2"):
                funcao = Funcao()
                self.lista_funcoes.append(funcao)
                self.lista_codigo.append( funcao.codigo )
            elif entrada.startswith("3"):
                flag = False
            
                
        

class Funcao:
    def __init__( self ):
        codigo = input(">>>Entre com a funcao: ")
        self.codigo = codigo

class DiagramaMl:
    def __init__( self ):
        pass


if __name__ == "__main__":
    obj_contrucao = Contrucao()
    for i in obj_contrucao:
        print( i )