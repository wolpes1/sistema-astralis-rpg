#Personagem do sistema de RPG criado por Renan Lopes Cavalcante

class Personagem_jogador:
    
    #Aspectos principais da classe

    def __init__(self, nome = str, jogador = str, forca = 0, habilidade = 0, vitalidade = 0, resistencia = 0, inteligencia = 0, afinidade_magica = 0, per_luta = '', per_mira = '', per_furt = '', per_pers = '', per_atle = '', per_sobr = '', per_conh = '', per_comu = '', per_inve = '', per_dano = '', per_auxi = ''):

        self.nome = nome
        self.jogador = jogador
        self.forca = forca
        self.habilidade = habilidade
        self.vitalidade = vitalidade
        self.resistencia = resistencia
        self.inteligencia = inteligencia
        self.afinidade_magica = afinidade_magica
        self.pericia_luta = per_luta
        self.pericia_mira = per_mira
        self.pericia_furtividade = per_furt
        self.pericia_persuasao = per_pers
        self.pericia_atletismo = per_atle
        self.pericia_sobrevivencia = per_sobr
        self.pericia_conhecimentos = per_conh
        self.pericia_comunicacao = per_comu
        self.pericia_investigacao = per_inve
        self.pericia_magia_dano = per_dano
        self.pericia_magia_auxilio = per_auxi
        self.luta = forca + self.treino(self.pericia_luta)
        self.mira = habilidade + self.treino(self.pericia_mira)
        self.furtividade = habilidade + self.treino(self.pericia_furtividade)
        self.persuasao = habilidade + self.treino(self.pericia_persuasao)
        self.atletismo = resistencia + self.treino(self.pericia_atletismo)
        self.sobrevivencia = resistencia + self.treino(self.pericia_sobrevivencia)
        self.conhecimentos = inteligencia + self.treino(self.pericia_conhecimentos)
        self.comunicacao = inteligencia + self.treino(self.pericia_comunicacao)
        self.investicacao = inteligencia + self.treino(self.pericia_investigacao)
        self.magia_dano = afinidade_magica + self.treino(self.pericia_magia_dano)
        self.magia_auxilio = afinidade_magica + + self.treino(self.pericia_magia_auxilio)
        self.pv_total = (vitalidade * 3) + self.sobrevivencia + self.treino(self.pericia_sobrevivencia)
        self.pm_total = afinidade_magica * 2
        self.iniciativa = habilidade

    #Retornos dos atributos contidos na classe


    def nome(self):
        return self.nome
    
    def jogador(self):
        return self.jogador
    
    def mostrar_vida(self):
        return f"Seus pontos de vida são: {self.pv_total}"
    
    def status(self):
        self.status = f"""Força = {self.forca}
        Habilidade = {self.habilidade}
        Vitalidade = {self.vitalidade}
        Resistência = {self.resistencia}
        Inteligência = {self.inteligencia}
        Afinidade Mágica = {self.afinidade_magica}"""
        return self.status


    def __str__(self):
        return f"""
        Personagem: {self.nome}, pertence a {self.jogador}
        Seus status são:
        {self.status}"""
    
    #Atribuições de atributos da classe
    
    def definir_nome(self, nome_carregado):
        self.nome = nome_carregado

    def definir_jogador(self, jogador_carregado):
        self.jogador = jogador_carregado

    def definir_for(self,valor):
        self.forca = valor

    def definir_hab(self,valor):
        self.habilidade = valor
    
    def definir_vit(self,valor):
        self.vitalidade = valor

    def definir_int(self,valor):
        self.inteligencia = valor

    def definir_res(self,valor):
        self.resistencia = valor

    def definir_afi(self,valor):
        self.afinidade_magica = valor

    #funções gerais

    def treino(self, treinamento):
        if treinamento.lower() == "sim":
            return 2
        else:
            return 0
    