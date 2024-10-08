# class Conta:
#     def __init__(self, nro_agencia, saldo=0):
#         self._saldo = saldo
#         self.nro_agencia = nro_agencia

#     def depositar(self, valor):
#         # ...
#         self._saldo += valor

#     def sacar(self, valor):
#         # ...
#         self._saldo -= valor


#     def mostrar_saldo(self):
#         return self._saldo

# conta = Conta('001',100)
# conta.depositar(100)
# print(conta.nro_agencia, conta.mostrar_saldo())


#============= Propiedades ===============
# class Foo:
#     def __init__(self, x = None):
#         self._x = x

#     @property
#     def x(self):
#         return self._x or 0
    
#     @x.setter
#     def x(self, value):
#         self._x += value

#     @x.deleter
#     def x(self):
#         self._x = -1

    
# foo = Foo(10)
# print(foo.x)
# foo.x = 10
# print(foo.x)
# del foo.x
# print(foo.x)


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa('Bruno', 1999)
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade}')
