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

    #Retornos dos atributos contidos na classe


    def nome(self):
        return self.nome
    
    def jogador(self):
        return self.jogador

    def __str__(self):
        return f"""
        Personagem: {self.nome}, pertence a {self.jogador}
        Seus status são:
        Força => {self.forca}
        Habilidade => {self.habilidade}
        Vitalidade => {self.vitalidade}
        Resistência => {self.resistencia}
        Inteligência => {self.inteligencia}
        Afinidade Mágica => {self.afinidade_magica}"""
    
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


    