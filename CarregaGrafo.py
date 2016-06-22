import sys
from Disciplina import Disciplina
from Curso import Curso

class CarregaGrafo:
    
    def __init__(self):
        self.lista_pre_requitos = {}
        self.lista_disciplinas = []
        self.dic_lista_disciplinas = {}
                
           
    def adicionar_pre_requisito(self, codigo_disciplina, codigo_pre_requisito):
        if not codigo_disciplina in self.lista_pre_requitos:
            self.lista_pre_requitos[codigo_disciplina] = []
        self.lista_pre_requitos[codigo_disciplina].append(codigo_pre_requisito)
    
    
    def recupera_dic_lista_disciplina(self, codigo_disciplina):
        if codigo_disciplina in self.dic_lista_disciplinas:
            return self.lista_pre_requitos[codigo_disciplina]
        else:
            return []
    
    def carrega (self, nomeCurso):
       
        
        try:
                 
            arquivo = open(nomeCurso + '.txt', 'r')
            #arquivo = open('engenharia de computacao.txt', 'r')
            nomeC = (arquivo.readline()).split(': ')
            nomeC = nomeC[1]
            #print(nomeC)
            numeroDeSemestre = (arquivo.readline()).split(': ')
            numeroDeSemestre = numeroDeSemestre[1]
            #print(numeroDeSemestre)
            nomeDepart = (arquivo.readline()).split(': ')
            nomeDepart = nomeDepart[1]
            #print(nomeDepart)
            arquivo.readline()
            
            C = Curso(nomeC, numeroDeSemestre, nomeDepart)
            
            
            informacao = arquivo.readline()
            controle = '*' in informacao
            
           
            while (informacao != '##'):
               
                    
                #print(informacao)
                informacao = informacao.split('\t')
                C.adicionar_disciplina(informacao[0])
                C.dic_adicionar_disciplina(informacao[0], informacao[1])
                C.dic_adicionar_disciplina(informacao[0], informacao[2])
                C.dic_adicionar_disciplina(informacao[0], informacao[3])
                D = Disciplina(informacao[0], informacao[1], informacao[2], informacao[3])
                
                #print(informacao)
                
                
                    
                i = 4
                if informacao[i] != '\n':
                    vertice = informacao[0]
                    while informacao[i] != '\n':
                        
                        self.adicionar_pre_requisito(vertice, informacao[i])
                        #D.adicionar_pre_requisito(int(vertice), int(informacao[i]))
                        #print('vertice:'+informacao[0])
                        #print(informacao[i])
                        
                        i = i + 1
                   
                
                informacao = arquivo.readline()
                controle = '*' in informacao
                if controle:
                    controle = True
                    informacao = arquivo.readline()
            
            
            D.lista_pre_requitos = self.lista_pre_requitos.copy()
            self.lista_disciplinas = C.lista_disciplinas.copy()
            self.dic_lista_disciplinas = C.dic_lista_disciplinas.copy()
                    
                 
            arquivo.close()
            
            #print(C.lista_disciplinas)
            #print(D.lista_pre_requitos)
            #print(C.dic_lista_disciplinas)
           
           
        except IOError:
            print ("I/O error({0}): {1}")
        except ValueError:
            print ("erro conversao de dados")
        except:
            print ("erro inesperado"), sys.exc_info()[0]
            raise
        
    
    