# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
    
#     def depositar(self, valor):
#         self.saldo += valor
#         print(f'Você depositou {valor}')

#     def sacar(self, valor):
#         if valor > self.saldo:
#             print('Saldo insuficiente!')
#         else:
#             self.saldo -= valor
#             print(f'Você sacou {valor}')

#     def exibir_saldo(self):
#         print(f'Seu saldo é: {self.saldo}')
    
# user = ContaBancaria('Bruno', 0)
# user.depositar(500)
# user.sacar(300)
# user.exibir_saldo()

# -------------------------------------------------------------------

# class Retangulo:
#     def __init__(self, largura:float, altura:float):
#         self.largura = largura
#         self.altura = altura

#     def area(self):
#         return self.largura * self.altura
    
#     def perimetro(self):
#         return (self.largura * 2) + (self.altura * 2)
    
# retangulo = Retangulo(10, 25)
# print(f'Área: {retangulo.area()}')
# print(f'Perimetro: {retangulo.perimetro()}')

# --------------------------------------------------------------------

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def cumprimentar(self):
#         return f'Olá {self.nome}'
    
# class Aluno(Pessoa):
#     def estudar(self):
#         return f'O aluno {self.nome} está estudando'
    
# aluno = Aluno('Bruno', 25)
# print(aluno.cumprimentar())
# print(aluno.estudar())

#-----------------------------------------------------------------------

# class Livro:
#     def __init__(self, titulo, autor):
#         self.titulo = titulo
#         self._autor = autor

#     @property
#     def autor(self):
#         return self._autor

# class Biblioteca(Livro):
#     def __init__(self):
#         self.livros = []
        
#     def adicionar_livro(self, livro):
#         self.livros.append(livro)
#         return f'O livro "{livro.titulo}" foi adicionado com exito!'

#     def remover_livro(self, livro):
#         if livro in self.livros:
#             self.livros.remove(livro)
#             return f'Livro "{livro.titulo}" removido com sucesso!'
#         else:
#             return f'Livro "{livro.titulo}" não está na biblioteca'
    
#     def listar_livros(self):
#         if not self.livros:
#             return 'A biblioteca está vazia!'
        
#         return f'Livros na Biblioteca:\n' + '\n'.join([f'{livro.titulo} de {livro.autor}' for livro in self.livros])
    
# livro1 = Livro('Uma Loucura na Idade Media', 'Bruno Erick')
# livro2 = Livro('Uma aventura', 'Desconhecido')

# biblioteca = Biblioteca()
# print(biblioteca.adicionar_livro(livro1))
# print(biblioteca.adicionar_livro(livro2))
# print(biblioteca.listar_livros())
# print(biblioteca.remover_livro(livro1))
# print(biblioteca.listar_livros())

# ---------------------------------------------------------------

class Funcionario:
    def __init__(self, nome:str, cargo:str, salario:float):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
        return f'Funcionario {funcionario.nome} adicionado com sucesso!'
    
    def remover(self, funcionario: Funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            return f'Funcionario {funcionario.nome} removido com sucesso!'
        else:
            return f'Funcionario {funcionario.nome} não encontrado!'
        
    def listar_funcionarios(self):
        if not self.funcionarios:
            return 'A lista de funcionarios está vazia!'
        return f'Funcionarios na Lista de Funcionarios:\n' + '\n'.join([f'{funcionario.nome} - {funcionario.cargo}' for funcionario in self.funcionarios])

nome = input('Digite o nome do Funcionário: ')
cargo = input('Digite o cargo do funcionario: ')
salario = float(input('Digite o salario do Funcionario: '))

funcionario = Funcionario(nome, cargo, salario)

empresa = Empresa()
empresa.adicionar(funcionario)

print(empresa.listar_funcionarios())
