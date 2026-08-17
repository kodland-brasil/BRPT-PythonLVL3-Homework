# Informações sobre gamers

Olá. Estamos construindo uma plataforma para jogos online e precisamos de ajuda para armazenar, processar e usar informações sobre nossos gamers. Este ano, daremos a vocês algumas tarefas para implementar; esta aqui é a primeira delas. Não se esqueça de olhar o arquivo README.md toda vez - nele, você encontrará requisitos detalhados e dicas!

## TAREFA 1. Refinamento da classe Gamer e implementação da ferramenta para adicionar dados do usuário

Nós já criamos a classe Gamer. Ela nos permitirá processar as seguintes informações sobre os usuários: nome, idade e jogos favoritos. Essas informações serão exibidas como uma pequena apresentação organizada, permitindo que o gamer faça novos amigos! No entanto, há um problema - esquecemos de adicionar campos para o apelido (nickname) e e-mail do usuário... Você pode ajudar nossa equipe com esta tarefa? Se sim, aqui estão a lista de verificação da tarefa e algumas dicas!

### Lista de verificação TAREFA 1

 - [ ] Melhore a classe Gamer - adicione os campos **nickname** e **email**
 - [ ] Ajuste a mensagem da mini-apresentação para incluir os novos dados
 - [ ] Teste o código com o **teste Pytest** que preparamos para garantir que o código atende à nossa solicitação!

## Sobre os testes

### Teste Pytest

Nós escrevemos testes que verificam automaticamente a conformidade do código:

- `test_Task_1_name_and_age_check`: Verificamos se a classe "Gamer" ainda possui os atributos "name" e "age".
- `test_Task_2_add_nickname`: Verificamos se o atributo "nickname" foi adicionado à classe "Gamer".
- `test_Task_3_add_email`: Verificamos se o atributo "email" foi adicionado à classe "Gamer".
- `test_Task_4_change_message`: Testa a saída de informações para a mini-apresentação do gamer.

## Dicas

### Classes em Python

#### 1. Definindo uma classe:
```python
class NomeDaClasse:
    def __init__(self, parametros):
        # Construtor da classe
        self.campo1 = valor1
        self.campo2 = valor2
        # ...

    def metodo(self, parametros):
        # Definindo o método
        # ...

# Exemplo:
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
```
#### 2. Criando instâncias de classes:
```python
# Criação de instância da classe
objeto = NomeDaClasse(argumentos)

# Exemplo:
gato = Animal("Melvin", 3)
```
#### 3. Adicionando campos a uma classe:
```python
# Adicionando novos campos a uma classe
seuObjeto.novoCampo = valor

# Exemplo:
gato.cor = "laranja"
```
#### 4. Usando uma classe em um projeto:
```python
# Usando métodos e campos de uma classe
seuObjeto.metodo(argumentos) 
valor = seuObjeto.campo

# Exemplo:
gato.apresentar()
print(gato.cor)
```