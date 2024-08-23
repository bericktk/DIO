from classes import *

import textwrap

def menu():
    menu = '''\n
        ========================= MENU =======================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova Conta
        [lc]\tListar Contas
        [nu]\tNovo Usuário
        [q]\tSair
        => '''
    
    return input(textwrap.dedent(menu))

def depositar(valor, saldo, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f'Depósito: \tR$ {valor:.2f}\n'
            print(f'Depósito de R$ {valor:.2f} Realizado com Sucesso!')
    else:
        print('Operação deu erro! Valor informado inválido.')
    return saldo, extrato

def sacar(*, saque, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_excedido = saque > saldo
    limite_excedido = saque > limite
    saque_excedido = numero_saques >= limite_saques

    if saldo_excedido:
        print('Operação deu erro! Saldo insuficiente.')
    
    elif limite_excedido:
        print('Operação deu erro! Valor do SAQUE excede o LIMITE.')

    elif saque_excedido:
        print('Operação deu erro! Numero máximo de SAQUES excedido.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: \t\tR$ {saque:.2f}\n'
        numero_saques += 1
        print(f'Saque de R$ {saque:.2f} Realizado com Sucesso!')
    
    else:
        print('Operação deu erro! O valor informado é inválido.')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n================== EXTRATO ==================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('===============================================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF(somente números): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\n Já existe usuário com esse CPF! ')
        return

    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradour, nro = bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereco})

    print('======== Usuario Cadastrado com Sucesso =========')

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\nConta Criada com Sucesso! ')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario':usuario}
    print('\n Usuário não encontrado, fluxo de criação de conta encerrado! ')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    '''
        
    print('='*100)
    print(textwrap.dedent(linha))

def main():
    limite_saques = 3
    agencia = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    

    while True:
        op = menu()

        if op == 'd':
            valor = float(input('Digite o valor do Depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif op == 's':
            saque = float(input('Informe o valor para saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )

        elif op == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif op == 'nu':
            criar_usuario(usuarios)

        elif op == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif op == 'lc':
            listar_contas(contas)

        elif op == 'q':
            break

        else:
            print('Opção invalida, tente novamente!')

main()
