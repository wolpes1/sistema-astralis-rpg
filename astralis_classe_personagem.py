#Personagem do sistema de RPG criado por Renan Lopes Cavalcante

class Personagem_jogador:

    #Aspectos principais da classe

    def __init__(self, nome = str, jogador = str, forca = 0, habilidade = 0, vitalidade = 0, resistencia = 0, inteligencia = 0, afinidade_magica = 0):
        self.nome = nome
        self.jogador = jogador
        self.forca = forca
        self.habilidade = habilidade
        self.vitalidade = vitalidade
        self.resistencia = resistencia
        self.inteligencia = inteligencia
        self.afinidade_magica = afinidade_magica
        self.magias = []

    #Retornos dos atributos contidos na classe

    def nome(self):
        return self.nome
    
    def jogador(self):
        return self.jogador
    
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
        Força = {self.forca}
        Habilidade = {self.habilidade}
        Vitalidade = {self.vitalidade}
        Resistência = {self.resistencia}
        Inteligência = {self.inteligencia}
        Afinidade Mágica = {self.afinidade_magica}
        Magias = {self.magias}"""
    
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

    def adicionar_magia(self, magia):
        self.magias.append(magia)

    