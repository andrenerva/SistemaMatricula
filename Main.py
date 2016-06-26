from Disciplina import Disciplina
from Curso import Curso
from Arquivo import Arquivo
from CarregaGrafo import CarregaGrafo
from cProfile import label
from distutils.log import INFO


if __name__ == '__main__':
    
    while True:
        
        A = Arquivo()
        CG = CarregaGrafo()
        D = Disciplina(None, None, None, None)
        
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
    
            A.criarArq('Fluxo' + nomeCurso)    
            listaFluxo = D.listar_disciplinas_nao_cursadas.copy()     
            
            contadorDecreditos = 0
            semestre = 2
            A.gravarNoArq('Fluxo' + nomeCurso, '********************** semestre *********************************\n' ) 
            semestre = semestre + 1
            creditos_restantes = 0
            lista_semestre = []
            
            while listaFluxo != []:
                
                codDisciplina = listaFluxo[0]
        
                informacoes_disciplina = CG.dic_lista_disciplinas.get(codDisciplina)
                credito = int(informacoes_disciplina[1])
                lista_se_possui_pre_requisito = D.recupera_pre_requisitos(codDisciplina)
                
                contadorDecreditos = contadorDecreditos + credito
                listaFluxo_auxiliar = listaFluxo.copy()
                
                                
                if credito > creditos_restantes:
                
                    tamanho_lista_auxiliar = len(listaFluxo_auxiliar)
                
                    while ((creditos_restantes > 0) and (tamanho_lista_auxiliar >= 0)):
                        
                        for cod_disciplina in listaFluxo_auxiliar:
                            
                            informacoes_disciplina_complemento = CG.dic_lista_disciplinas.get(cod_disciplina)
                            creditos_complemento = int(informacoes_disciplina_complemento[1])
                            
                            if creditos_complemento <= creditos_restantes:
                                contadorDecreditos = contadorDecreditos - credito                                
                                lista_pre_req = D.recupera_pre_requisitos(cod_disciplina)
                                
                                if len(lista_pre_req) == 0:
                                    A.gravarNoArq('Fluxo' + nomeCurso, cod_disciplina + '\t')
                                    A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina_complemento[0] + '\t')
                                    A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina_complemento[1] + '\t')
                                    A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina_complemento[2] + '\n')
                                    listaFluxo.remove(cod_disciplina)
                                    creditos_restantes = creditos_restantes - creditos_complemento
                                    contadorDecreditos = contadorDecreditos + creditos_complemento
                                    
                                    if contadorDecreditos >= credMax:
                                        contadorDecreditos = credMax + 1
                                    
                                    break
                                    
                                else:
                                    achou = 0
                                    
                                    for cod in listaFluxo_auxiliar:
                                        for pre_req in lista_pre_req:
                                            if cod == pre_req:
                                                achou = 1
                                            
                                    if achou == 0:        
                                        A.gravarNoArq('Fluxo' + nomeCurso, cod_disciplina + '\t')
                                        A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina_complemento[0] + '\t')
                                        A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina_complemento[1] + '\t')
                                        A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina_complemento[2] + '\n')
                                        listaFluxo.remove(cod_disciplina)
                                        creditos_restantes = creditos_restantes - creditos_complemento
                                        contadorDecreditos = contadorDecreditos + creditos_complemento
                                        break
                                        
                        tamanho_lista_auxiliar = tamanho_lista_auxiliar - 1
                                    
                if contadorDecreditos <= credMax:
                
                    creditos_restantes = credMax - contadorDecreditos
                
                    if len(lista_se_possui_pre_requisito) == 0:
                        A.gravarNoArq('Fluxo' + nomeCurso, codDisciplina + '\t')
                        A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[0] + '\t')
                        A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[1] + '\t')
                        A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[2] + '\n')
                        lista_semestre.append(codDisciplina)
                        listaFluxo.remove(codDisciplina)
                        
                    else:
                        achou = 0
                        achou_no_mesmo_semestre = 0
                        
                        for cod in listaFluxo:
                            for pre_req in lista_se_possui_pre_requisito:
                                if cod == pre_req:
                                    achou = 1
                                    
                        for cod in lista_semestre:
                            for pre_req in lista_se_possui_pre_requisito:
                                if cod == pre_req:
                                    achou_no_mesmo_semestre = 1            
                        
                        if achou_no_mesmo_semestre == 1:
                            listaFluxo.remove(codDisciplina)
                            if len(listaFluxo) < 5:
                                listaFluxo.insert(1, codDisciplina)
                                contadorDecreditos = contadorDecreditos - credito
                            else:
                                listaFluxo.insert(5, codDisciplina)
                                contadorDecreditos = contadorDecreditos - credito
                        else: 
                            if achou == 0:
                                A.gravarNoArq('Fluxo' + nomeCurso, codDisciplina + '\t')
                                A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[0] + '\t')
                                A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[1] + '\t')
                                A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[2] + '\n')
                                lista_semestre.append(codDisciplina)
                                listaFluxo.remove(codDisciplina)
                
                if contadorDecreditos > credMax :
                    
                    contadorDecreditos = 0
                    lista_semestre = []
                    
                    A.gravarNoArq('Fluxo' + nomeCurso, '********************** semestre *********************************\n' )
                    
                    if len(lista_se_possui_pre_requisito) == 0:
                        A.gravarNoArq('Fluxo' + nomeCurso, codDisciplina + '\t')
                        A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[0] + '\t')
                        A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[1] + '\t')
                        A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[2] + '\n')
                        listaFluxo.remove(codDisciplina)
                        contadorDecreditos = credito
                        
                    else:
                        achou = 0
                        
                        for cod in listaFluxo:
                            for pre_req in lista_se_possui_pre_requisito:
                                if cod == pre_req:
                                    achou = 1
                        
                        if achou == 0:
                            A.gravarNoArq('Fluxo' + nomeCurso, codDisciplina + '\t')
                            A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[0] + '\t')
                            A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[1] + '\t')
                            A.gravarNoArq('Fluxo' + nomeCurso, informacoes_disciplina[2] + '\n')
                            listaFluxo.remove(codDisciplina)
                            contadorDecreditos = credito
                    
                    lista_semestre.append(codDisciplina)            
                            
            A.gravarNoArq('Fluxo' + nomeCurso, '*******************************************************************\n' )  
            A.lerSemestre('Fluxo' + nomeCurso)