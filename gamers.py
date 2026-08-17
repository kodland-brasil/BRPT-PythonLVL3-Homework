# Definição da classe "Gamer"
# Tarefa 2. Adicionar o campo nickname
# Tarefa 3. Adicionar o campo email
class Gamer:
    def __init__(self, name, age, nickname, email):
        self.name = name
        self.age = age

        self.games = []

    def add_game(self, game):
        self.games.append(game)

    # Tarefa 4: Alterar a mensagem
    def introduce(self):
        print(f"Olá, meu nome é {self.name}, eu tenho {self.age} anos.")


# Criando uma instância da classe "Gamer"
gamer1 = Gamer("João", 14, "JoaoForever", "joao@gmail.com")

# Adicionando jogos
gamer1.add_game("Minecraft")
gamer1.add_game("Dota 2")

# Mini-apresentação do gamer
gamer1.introduce()

# Exibindo os jogos favoritos
print(f"{gamer1.name} gosta destes jogos: {', '.join(gamer1.games)}")