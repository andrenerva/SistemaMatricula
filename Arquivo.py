class Arquivo:
    
    
    def criarArq (self, nomeCurso):
        arquivo = open(nomeCurso + '.txt', 'w')
        arquivo.close()
        
            
    def gravarNoArqCabecalho(self, nomeCurso, nr_semestres, departamento):
        arquivo = open(nomeCurso + '.txt', 'r')
        texto = arquivo.readlines()
        informacao = ('Nome do curso: '+ nomeCurso +'\n')
        texto.append(informacao)
        informacao = ('Numero total de semestre: ' + str(nr_semestres) +'\n')
        texto.append(informacao)
        informacao = ('Departamento do curso: ' + departamento + '\n')
        texto.append(informacao)
        
        arquivo = open(nomeCurso + '.txt', 'w')
        arquivo.writelines(texto)
        arquivo.close() 
        
        
    def gravarNoArq (self, nomeCurso, informacao):
        arquivo = open(nomeCurso + '.txt', 'r')
        texto = arquivo.readlines()
        texto.append(informacao)
        
         
        arquivo = open(nomeCurso + '.txt', 'w')
        arquivo.writelines(texto)
        arquivo.close() 
                              
    