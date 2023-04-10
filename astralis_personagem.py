#Personagem do sistema de RPG criado por Renan Lopes Cavalcante

class Personagem_jogador:
    
    #Definição dos aspectos principais da classe
    def __init__(self, nome = str, jogador = str, status = {"Força":0,"Habilidade":0, "Vitalidade": 0, "Resistência": 0, "Inteligência": 0, "Afinidade Mágica": 0}, pericias = []):
        self.nome = nome
        self.jogador = jogador
        self.status = status

    def nome(self):
        return self.nome
    
    def jogador(self):
        return self.jogador

    #Definição da string que aparecerá caso necessário mostrar os aspectos gerais do personagem
    def __str__(self):
        return f"{self.nome}, pertence a {self.jogador}\nSeus status são:{self.status}"


    #Adicionando status
    def adicionar_força(self, quantidade_pontos = int):
        self.status["Força"] += quantidade_pontos
        print(f"Seu personagem ganhou #{quantidade_pontos} de força!")
    
    def adicionar_habilidade(self, quantidade_pontos = int):
        self.status["Habilidade"] += quantidade_pontos
        print(f"Seu personagem ganhou #{quantidade_pontos} de habilidade!")

    def adicionar_vitalidade(self, quantidade_pontos = int):
        self.status["Vitalidade"] += quantidade_pontos
        print(f"Seu personagem ganhou #{quantidade_pontos} de vitalidade!")

    def adicionar_resistencia(self, quantidade_pontos = int):
        self.status["Resistência"] += quantidade_pontos
        print(f"Seu personagem ganhou #{quantidade_pontos} de resistêcia!")

    def adicionar_inteligencia(self, quantidade_pontos = int):
        self.status["Inteligência"] += quantidade_pontos
        print(f"Seu personagem ganhou #{quantidade_pontos} de inteligência!")

    def adicionar_afinidade_magica(self, quantidade_pontos = int):
        self.status["Afinidade Mágica"] += quantidade_pontos
        print(f"Seu personagem ganhou #{quantidade_pontos} de Afinidade Mágica!")

