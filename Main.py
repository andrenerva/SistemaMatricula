from Disciplina import Disciplina
from Curso import Curso
from Arquivo import Arquivo
from CarregaGrafo import CarregaGrafo



if __name__ == '__main__':
    A = Arquivo()
    CG = CarregaGrafo()
    D = Disciplina(None, None, None, None)
   
    
    while True:
        print('*************************** Menu *******************************')
        print('1 - Cadastrar curso')
        print('2 - Indicar Disciplinas cursadas')
        #print('3 - Indicar Disciplinas cursadas')
        print('****************************************************************\n')
        opcao = input('Selecione uma opcao: ' )
        
        if opcao is '1':
            nome = input('Digite o nome do curso: ')
            departamento = input('Digite o departamento: ')
            nro_semestres = input('Digite o numero de semestres: ')
            
            nro_semestres = int(nro_semestres)
            
            C = Curso(nome,nro_semestres, departamento)
            A.criarArq(nome)
            A.gravarNoArqCabecalho(nome, nro_semestres, departamento)
            
            i = 0
            
            while i < nro_semestres:
                controle1 = True
                i = i+1
            
                print("******************* %d semestre****************************" %i)
                A.gravarNoArq(C.nome, '******************** Semestre '+str(i) +' ********************' +'\n')

                while controle1:
                
                    controle= True
                    contadorDisciplina = 0
                    
                    codigo = input("Digite o codigo da disciplina:")                   
                    nome = input("Digite o nome da disciplina:")                  
                    nro_creditos = input("Digite o numero de creditos:")                   
                    situacao = input("A disciplina e obrigatoria?")
                    
                    if situacao is 's':
                        tipo = 'OBR' 
                    else: 
                        tipo = 'OPT'
                        
                
                    D = Disciplina(nome, nro_creditos, codigo, situacao)
                    C.adicionar_disciplina(D.codigo)
                    
                    cod_dis = str(D.codigo)
                    A.gravarNoArq(C.nome, cod_dis +'\t')
                    A.gravarNoArq(C.nome, D.nome +'\t')
                    creditos = str(D.nro_creditos) 
                    A.gravarNoArq(C.nome, creditos +'\t')
                    if situacao is 's':
                        A.gravarNoArq(C.nome, tipo +'\t')
                    else: 
                        A.gravarNoArq(C.nome, tipo +'\t')
                    
                    
                    controle = input("Possui pre-requisitos?")
                
                    if controle is 's':
                        
                        while controle:
                            pre_requisito = input("Digite o codigo do pre-requisito?")
                            
                            D.adicionar_pre_requisito(D.codigo, str(pre_requisito))
                            codigos = D.lista_pre_requitos.pop(D.codigo)
                            
                            for cod in codigos:
                                codigo_pre = str(cod)
                                A.gravarNoArq(C.nome, codigo_pre + '\t')
                                
                           
                        
                            controle = input("Possui outro pre-requisitos?")
                            
                            if controle is 's':
                                controle = True
                                
                            if controle is 'n':
                                controle = False
                                A.gravarNoArq(C.nome,'\n')
                                controle2= input("Deseja cadastrar mais uma disciplina no semestre %d?" %i)
                                if controle2 is 'n':
                                    controle1 = False
                                                               
                    if controle is 'n':
                        controle = False
                        A.gravarNoArq(C.nome,'\n')
                        controle2= input("Deseja cadastrar mais uma disciplina no semestre %d?" %i)
                        if controle2 is 'n':
                            controle1 = False
                            
            A.gravarNoArq(C.nome,'##')
            print('*****Curso de %s cadastrado com sucesso!!*****' %C.nome) 
            
            
            
            
        if opcao is '3':
           
           
            
            CG = CarregaGrafo()
            CG.carrega('engenharia de computacao')
            
        if opcao is '2':
            CG = CarregaGrafo()
            nomeCurso = input('Digite o nome do seu curso:')
            CG.carrega(nomeCurso)
            
            
        
            print('***********************************************************') 
            for cod in CG.lista_disciplinas:
                resposta = input('voce ja cursou %s?' %CG.dic_lista_disciplinas.get(cod)[0])
                if resposta is 's':
                    D.adicionar_disciplinas_cursadas(cod)
                else:
                    D.adicionar_disciplinas_nao_cursadas(cod)
                
            print('disciplinas cursadas: %s' %D.listar_disciplinas_cursadas)
            print('disciplinas nao cursadas: %s' %D.listar_disciplinas_nao_cursadas)
           
            
            
    
            for disciplina_nao_cursada in D.listar_disciplinas_nao_cursadas:
                if CG.lista_pre_requitos.__contains__(disciplina_nao_cursada) is False:
                
                    D.adicionar_disciplinas_a_ser_cursadas(disciplina_nao_cursada)
                else:
                    print('fazer com as disciplinas com pre requisito')
                    lista_para_ser_verificada = D.adicionar_disciplinas_a_ser_verificadas(disciplina_nao_cursada)
                          
                        
                    
                
            
                
                    
                    
            
            print('disciplinas a serem cursadas: %s' %D.lista_disciplinas_a_ser_cursadas) 
            print('disciplinas a serem verificadas %s' %D.lista_disciplinas_a_ser_verificadas)  
                
            