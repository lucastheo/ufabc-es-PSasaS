class Contrucao:
    def __init__(self ):
        self.lista_classes = list()
        self.lista_funcoes = list()
        self.lista_codigo = list()

    def __iter__( self ):
        return self

    def __next__( self ):
        print("<<<Possiveis tipos de entrada")
        print("<<<\tCodigo 1")
        print("<<<\tFuncao/Metodo 2")
        print("<<<\tClasse 3")

        i = input("\nQual tipo de entrada? ")

        if i.startswith('1'):
            codigo = input("Entre com o codigo: ")
            self.lista_codigo.append( codigo )
        elif i.startswith('2'):
            funcao = Funcao( )
            self.lista_funcoes.append( funcao )
            self.lista_codigo.append( funcao.codigo )
        elif i.startswith('3'):
            classe = Classes( )
            self.lista_classes.append( classe )
            for funcao in classe.lista_funcoes:
                self.lista_funcoes.append( funcao )
                self.lista_codigo.append( codigo )


class Classes:
    def __init__( self ):
        self.lista_funcoes = list()
        self.codigo = ''

class Funcao(str):
    def __init__( self ):
        self.codigo = ''

