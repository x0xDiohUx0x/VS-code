class Personagem:
    def __init__(self, tipo, nome, idade, ataque):
        self.tipo = tipo
        self.nome = nome
        self.idade = idade
        self.ataque = ataque
        
    def escrever(self):
        print(f"O {self.tipo} {self.nome} atacou usando {self.ataque}")

# Criando uma instância da classe Personagem
personagem1 = Personagem("Mago", "White", 64, "Magia")
personagem2 = Personagem("Guerreiro", "Black", 32, "coronhada")
# Chamando o método escrever

personagem1.escrever()
personagem2.escrever()