class Curso:
    
    def __init__(self, nome, nro_semestres, departamento):
        self.nome = nome
        self.nro_semestres = nro_semestres
        self.departamento = departamento
        self.lista_disciplinas = []
        self.dic_lista_disciplinas = {}
        
    
    def adicionar_disciplina(self, disciplina):
        self.lista_disciplinas.append(disciplina)
    
    def dic_adicionar_disciplina(self, codigo_disciplina, informacao):
        if not codigo_disciplina in self.dic_lista_disciplinas:
            self.dic_lista_disciplinas[codigo_disciplina] = []
        self.dic_lista_disciplinas[codigo_disciplina].append(informacao)