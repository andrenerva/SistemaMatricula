from Disciplina import Disciplina
from Curso import Curso
from Arquivo import Arquivo
from CarregaGrafo import CarregaGrafo
from cProfile import label


if __name__ == '__main__':
    
    A = Arquivo()
    CG = CarregaGrafo()
    D = Disciplina(None, None, None, None)
    
    while True:
        
        print('*************************** Sistema de Matriculas *******************************\n')
        print('(1) Cadastrar curso')
        print('(2) Simular fluxo do semestre')
        print('(3) Simular fluxo completo ')
        print('\n********************************************************************************\n')
        opcao = input('Selecione a opcao desejada: ' )
        
        if opcao is '1':
            
            print('\n-> Cadastrar curso\n')
            nome = input('Entre com o nome do curso:\n')
            departamento = input('Entre com o departamento do curso:\n')
            nro_semestres = input('Entre com o numero de semestres do curso:\n')
            
            nro_semestres = int(nro_semestres)
            
            C = Curso(nome,nro_semestres, departamento)
            
            A.criarArq(nome)
            A.gravarNoArqCabecalho(nome, nro_semestres, departamento)
            
            i = 0
            
            while i < nro_semestres:
                
                controle1 = True
                i = i+1
            
                print("\n-> Cadastrar disciplinas do %do semestre\n" %i)
                A.gravarNoArq(C.nome, '******************** Semestre '+str(i) +' ********************' +'\n')

                while controle1:
                
                    controle= True
                    contadorDisciplina = 0
                    
                    codigo = input("Entre com o codigo da disciplina:\n")                   
                    nome = input("Entre com o nome da disciplina:\n")                  
                    nro_creditos = input("Entre com o numero de creditos:\n")                   
                    situacao = input("A disciplina e obrigatoria? (s/n)\n")
                    
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
                    
                    
                    controle = input("A disciplina possui pre-requisitos? (s/n)\n")
                
                    if controle is 's':
                        
                        while controle:
                            
                            pre_requisito = input("Entre com o codigo do pre-requisito:\n")
                            
                            D.adicionar_pre_requisito(D.codigo, str(pre_requisito))
                            codigos = D.lista_pre_requitos.pop(D.codigo)
                            
                            for cod in codigos:
                                codigo_pre = str(cod)
                                A.gravarNoArq(C.nome, codigo_pre + '\t')
                                                        
                            controle = input("A disciplina possui outro pre-requisitos? (s/n)\n")
                            
                            if controle is 's':
                                controle = True
                                
                            if controle is 'n':
                                controle = False
                                A.gravarNoArq(C.nome,'\n')
                                controle2= input("\n>> Deseja cadastrar mais uma disciplina no semestre %d? (s/n)\n" %i)
                                if controle2 is 'n':
                                    controle1 = False
                                                               
                    if controle is 'n':
                        controle = False
                        
                        A.gravarNoArq(C.nome,'\n')
                        controle2= input("\n>> Deseja cadastrar mais uma disciplina no semestre %d? (s/n) \n" %i)
                        
                        if controle2 is 'n':
                            controle1 = False
                            
            A.gravarNoArq(C.nome,'##')
            print('\n*****Curso - %s - cadastrado com sucesso!!*****\n' %C.nome) 
            
        if opcao is '3':
            nomeCurso = input('Entre com o nome do curso desejado:\n')
            A.lerArquivo('Fluxo' + nomeCurso)
            
        if opcao is '2':
            
            print ('\n-> Simular fluxo\n')
            
            CG = CarregaGrafo()
            C = Curso(None, None, None)
            C.dic_lista_disciplinas = CG.dic_lista_disciplinas.copy()
            nomeCurso = input('Entre com o nome do curso desejado:\n')
            credMax = int(input("Informe o numero maximo de credito por semestre: "))
            CG.carrega(nomeCurso)
            D.lista_pre_requitos = CG.lista_pre_requitos.copy()
            
            print('\n-> Selecione as disciplinas cursadas e que o aluno aprovou, com - s -, caso contrario - n') 
            for cod in CG.lista_disciplinas:
                resposta = input('- %s? ' %CG.dic_lista_disciplinas.get(cod)[0])
                if resposta is 's':
                    D.adicionar_disciplinas_cursadas(cod)
                else:
                    D.adicionar_disciplinas_nao_cursadas(cod)
                
            #print('\n-> Lista de disciplinas cursadas pelo aluno: %s' %D.listar_disciplinas_cursadas)
            #print('-> Lista de disciplinas nao cursadas pelo aluno: %s' %D.listar_disciplinas_nao_cursadas)
           
            for disciplina_nao_cursada in D.listar_disciplinas_nao_cursadas:
                if CG.lista_pre_requitos.__contains__(disciplina_nao_cursada) is False:
                    D.adicionar_disciplinas_a_ser_cursadas(disciplina_nao_cursada)
                    
                if CG.lista_pre_requitos.__contains__(disciplina_nao_cursada) is True:
                    #print('fazer com as disciplinas com pre requisito')
                    lista_para_ser_verificada = D.adicionar_disciplinas_a_ser_verificadas(disciplina_nao_cursada)
                    
                    
                    
            for disciplina in D.lista_disciplinas_a_ser_verificadas:
                listaPre = D.recupera_pre_requisitos(disciplina)
                resposta = D.possui_os_pre_requisitos(listaPre)
                if resposta is True:
                   D.adicionar_disciplinas_a_ser_cursadas(disciplina)
            
            contadorDecreditos = 0
            listaDisProposta = []
            listaFluxo = []
            A.criarArq('Fluxo'+ nomeCurso)
            semestre = 1
            A.gravarNoArq('Fluxo' + nomeCurso, '**********************  semestre *********************************\n' )
            semestre = semestre + 1
            for codDisciplina in D.lista_disciplinas_a_ser_cursadas: 
                    
                listaPreReq = CG.dic_lista_disciplinas.get(codDisciplina)
                credito = int(listaPreReq[1])
                contadorDecreditos = contadorDecreditos + credito
                
                if contadorDecreditos <= credMax :
                    
                    A.gravarNoArq('Fluxo' + nomeCurso, codDisciplina)
                    listaDisProposta.append(codDisciplina)
                    A.gravarNoArq('Fluxo' + nomeCurso, '\t')
                   
                    for informacao in listaPreReq :
                        A.gravarNoArq('Fluxo' + nomeCurso, informacao)
                        A.gravarNoArq('Fluxo' + nomeCurso, '\t' )
                
                    A.gravarNoArq('Fluxo' + nomeCurso, '\n')
                    
                    
            #print('-> Disciplinas a serem verificadas seus pre requisitos %s' %D.lista_disciplinas_a_ser_verificadas)   
            #print('-> Disciplinas a serem cursadas: %s' %D.lista_disciplinas_a_ser_cursadas) 
            print('VOCE DEVERA SEGUIR O SEMESTRE ABAIXO PARA CONCLUIR O CURSO EM MENOS TEMPO:\n')
            A.lerSemestre('Fluxo' + nomeCurso)
            print('UM ARQUIVO TEXTO COM ESSE FULXO FOI GERADO!!!')
            #print('-> Disciplinas a serem cursadas: %s' %CG.lista_disciplinas)
            
            
            #print(listaDisProposta)
            
            
            listaFluxo = CG.lista_disciplinas.copy()
            for cod1 in D.listar_disciplinas_cursadas:
                listaFluxo.remove(cod1)
            for cod2 in listaDisProposta:
                listaFluxo.remove(cod2)
            
            print('-> Disciplinas a serem cursadas removidas: %s' %CG.lista_disciplinas)
            
            
            #######################
            #######################
            ########################
            ########################
            
            contadorDecreditos = 0
            semestre = 2
            A.gravarNoArq('Fluxo' + nomeCurso, '********************** semestre *********************************\n' ) 
            semestre = semestre + 1
            
            for codDisciplina in listaFluxo: 
                
                
                    
                listaPreReq = CG.dic_lista_disciplinas.get(codDisciplina)
                credito = int(listaPreReq[1])
                contadorDecreditos = contadorDecreditos + credito
                
                if contadorDecreditos <= credMax :
                    
                
                    A.gravarNoArq('Fluxo' + nomeCurso, codDisciplina)
                    A.gravarNoArq('Fluxo' + nomeCurso, '\t')
                    
                    #print(credito)
                    #print(contadorDecreditos)
                    for informacao in listaPreReq :
                        A.gravarNoArq('Fluxo' + nomeCurso, informacao)
                        A.gravarNoArq('Fluxo' + nomeCurso, '\t' )
                
                    A.gravarNoArq('Fluxo' + nomeCurso, '\n')
                
                if contadorDecreditos > credMax :
                    
                    A.gravarNoArq('Fluxo' + nomeCurso, '********************** semestre *********************************\n' )
                    semestre = semestre + 1
                    
                    
                    if contadorDecreditos > credMax :
                        A.gravarNoArq('Fluxo' + nomeCurso, codDisciplina)
                        A.gravarNoArq('Fluxo' + nomeCurso , '\t')
                        
                        #print(credito)
                        #print(contadorDecreditos)
                        for informacao in listaPreReq :
                            A.gravarNoArq('Fluxo' + nomeCurso, informacao)
                            A.gravarNoArq('Fluxo' + nomeCurso, '\t' )
                        A.gravarNoArq('Fluxo' + nomeCurso, '\n')
                
                    contadorDecreditos = 0
                
                
                    
                
                
                
                
            A.gravarNoArq('Fluxo' + nomeCurso, '*******************************************************************\n' )  
            
            
            
        

            
            