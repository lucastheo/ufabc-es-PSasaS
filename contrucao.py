class Contrucao:

    def __str__( self ):
        s = ""
        for codigo in self.lista_codigo:
            s += str( codigo )
        for funcoes in self.lista_funcoes:
            s += str( funcoes )
        for classe in self.lista_classe:
            s += str( classe )
        for diagrama in self.lista_diagrama_Uml:
            s += str( diagrama )
        return s

    def __init__(self ):
        self.lista_classe = list()
        self.lista_funcoes = list()
        self.lista_codigo = list()
        self.lista_diagrama_Uml = list()

        flag = True
        while flag:
            print("<<<Possiveis tipos de entrada")
            print("\tCodigo 1")
            print("\tFuncao/Metodo 2")
            print("\tClasse 3")
            print("\tDiagrama ML 4")
            print("\tParar 5")

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
                diagrama_ml = DiagramaUml()
                self.lista_diagrama_Uml.append( diagrama_ml )
            elif entrada.startswith('5'):
                flag = False

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
   
    def __str__( self ):
        s = "Classe: [ "
        s += "Codigos: ["
        for i , codigo in  enumerate( self.lista_codigo ):
            s += f"\tCodigo {str( codigo )}"
        s += "] ,"
        s += " Funcoes: [ "
        for i , funcao in enumerate( self.lista_funcoes ):
            a = str( funcao ).strip("\n")
            s += f"{ a }"
        s+= " ]\n"
        return s

class Funcao:
    def __init__( self ):
        codigo = input(">>>Entre com a funcao: ")
        self.codigo = codigo
    def __str__( self ):
        s  = f"Funcao: ["
        s += f"Codigo{self.codigo} ]\n"
        return s

class DiagramaUml:
    def __init__( self ):
        diagrama = input(">>>Entre com o diagrama: ")
        self.diagrama = diagrama
    
    def __str__(self ):
        return f"Diagrama: {self.diagrama}\n"

if __name__ == "__main__":
    obj_contrucao = Contrucao()
    print( obj_contrucao )