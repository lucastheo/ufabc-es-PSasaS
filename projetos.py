import re
class Projeto:
    
    def __init__( self , lista_requisitos: list , nome:str , detalhes:str , custo:str , riscos:str ):
        self.lista_requisitos = lista_requisitos
        self.nome = nome
        self.detalhes = detalhes
        self.custo = custo
        self.riscos = riscos
        self.id = None
        self.validado = False
        self.lista_contrucao = list()

    def __str__( self ):
        s =  f'Projeto ({self.id})\n'
        s += f'\tNome: {self.nome}\n'
        s += f'\tDetalhes: {self.detalhes}\n'
        s += f"\tCusto: {self.custo}\n"
        s += f"\tRiscos: {self.riscos}\n" 

        return s
    def update_id( self , _id ):
        self.id = id
    def update_validado( self , validado ):
        self.validado
    
    def update_lista_contrucao( self , contrucao ):
        self.lista_contrucao.append( contrucao )
    

REGEX_COD_DE_REQUISTOS_VALIDA = '([([0-9]{1,}[ ]{0,1})*'
REGEX_NUMEROS = '[0-9]{1,}'

class PlanejarProjeto:
    def __init__( self , dict_todos_requisitos ):
        self.dict_todos_requisitos = dict_todos_requisitos
        self.lista_projetos = list()
    
    def __iter__( self ):
        return self

    def __next__( self ):
        i = input('>>>Gerar projeto(s/n)? ').lower()

        while i.startswith('s'):
            return self.novo()
        
        raise StopIteration

    def novo( self ):    
        cod_de_requisitos_do_projeto_str = input('>>>Quais requisitos vão gerar essa projeto? ')
    
        #Valida se os dados inputados são validos
        if re.fullmatch( REGEX_COD_DE_REQUISTOS_VALIDA , cod_de_requisitos_do_projeto_str ):
            
            #Corta as listas buscando os id's
            cod_de_requisitos_do_projeto = re.findall(REGEX_NUMEROS , cod_de_requisitos_do_projeto_str)
            
            #Retirando os conjuntos de requisitos do projeto
            lista_requisitos_do_projeto = list()
            for i in cod_de_requisitos_do_projeto:
                lista_requisitos_do_projeto.append( self.get_requisito( i ) )
            
            #Input dos dados
            nome = input('>>>Qual o nome do projeto? ')
            detalhes = input('>>>Passe os detalhes desse projeto: ')
            custos = input('>>>Passe os custos do projeto: ')
            riscos = input('>>>Passe os riscos do projeto: ')
            

            #Gera o projeto
            projeto = Projeto( lista_requisitos_do_projeto , nome , detalhes , custos , riscos )
            
            return projeto
        else:
            print('<<<Lista de requisitos invalida ')
    
    def get_requisito( self , i ):
        for tipo_requisito in self.dict_todos_requisitos:
            for requisito in self.dict_todos_requisitos[ tipo_requisito ]:
                return self.dict_todos_requisitos[ tipo_requisito ][ requisito ]

    def update_projeto( self , projeto ):
        self.lista_projetos.append( projeto )
        

def gerar_projeto( lista_todos_requisitos ):
    obj_planejar = PlanejarProjeto( lista_todos_requisitos )

    for projeto in obj_planejar:
        
        #Validando com cliente
        if input('>>>Projeto é viavel de ser feito? ').lower().startswith('s'):
            if input('>>>Aprovado pelo cliente mesmo apresentando os riscos e custos? ').lower().startswith('s'):
                projeto.update_validado(True)
                print('<<<Projeto pronto para ser executado')
                obj_planejar.update_projeto( projeto )
            else:
                print('<<<Projeto não deve ser executado')
        else:
            print('<<<Informar ao cliente que esse projeto não é viavel de ser feito')
            
    return obj_planejar            


if __name__ == '__main__':
    gerar_projeto(['AAAA', 'BBBB'])