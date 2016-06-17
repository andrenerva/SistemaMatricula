class Disciplina:
    
    def __init__(self, nome, nro_creditos, codigo, situacao):
        self.nome = nome
        self.nro_creditos = nro_creditos
        self.codigo = codigo
        self.situacao = situacao
        self.lista_pre_requitos = {}
        self.listar_disciplinas_cursadas = []
        self.listar_disciplinas_nao_cursadas = []
        self.lista_disciplinas_a_ser_cursadas = []
        self.lista_disciplinas_a_ser_verificadas = []
    
    
    
    #def  adicionar_pre_requisito(self, codigo_disciplina, codigo_pre_requisito):
        #self.lista_pre_requitos[codigo_disciplina] = codigo_pre_requisito
        
        
    def adicionar_pre_requisito(self, codigo_disciplina, codigo_pre_requisito):
        if not codigo_disciplina in self.lista_pre_requitos:
            self.lista_pre_requitos[codigo_disciplina] = []
        self.lista_pre_requitos[codigo_disciplina].append(codigo_pre_requisito)
        
    def recupera_pre_requisitos(self, codigo_disciplina):
        if codigo_disciplina in self.lista_pre_requitos:
            return self.lista_pre_requitos[codigo_disciplina]
        else:
            return []
    def adicionar_disciplinas_cursadas(self, cod_disciplina):
        self.listar_disciplinas_cursadas.append(cod_disciplina)
        
    def adicionar_disciplinas_nao_cursadas(self, cod_disciplina):
        self.listar_disciplinas_nao_cursadas.append(cod_disciplina)
    
    def adicionar_disciplinas_a_ser_cursadas(self, cod_disciplina):
        self.lista_disciplinas_a_ser_cursadas.append(cod_disciplina)
        
    def adicionar_disciplinas_a_ser_verificadas(self, cod_disciplina):
        self.lista_disciplinas_a_ser_verificadas.append(cod_disciplina)
        
        