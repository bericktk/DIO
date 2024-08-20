class Bicicleta: # Criando a classe
    def __init__(self, cor, modelo, ano, valor): #construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Pom pommmm')

    def parar(self):
        print('A bike ta parando!')
        print('Bike parada')

    def correr(self):
        print('Sai da frente... vrummmm')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


bike1 = Bicicleta('vermelha', 'caloi', 2022, 600)

bike1.buzinar()
bike1.correr()
bike1.parar()

def novaBike(): # Função para o Cliente adicionar uma nova Bike.
    cor = input('Digite a cor: ')
    modelo = input('Digite o modelo: ')
    ano = int(input('Digite o ano da Bike: '))
    valor = float(input('Qual o valor da bike: '))

    novaBike = Bicicleta(cor, modelo, ano, valor)
    print(novaBike)

novaBike()
