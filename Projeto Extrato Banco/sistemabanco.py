menu = '''
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while True:
    op = input(menu)

    if op == 'd':
        valor = float(input('Digite o valor do Depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'Depósito de R$ {valor:.2f} Realizado com Sucesso!')

        else:
            print('Operação deu erro! Valor informado inválido.')

    elif op == 's':
        saque = float(input('Informe o valor para saque: '))
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
            extrato += f'Saque: R$ {saque:.2f}\n'
            numero_saques += 1
            print(f'Saque de R$ {saque:.2f} Realizado com Sucesso!')
        
        else:
            print('Operação deu erro! O valor informado é inválido.')

    elif op == 'e':
        print('\n================== EXTRATO ==================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===============================================')

    elif op == 'q':
        break

    else:
        print('Opção invalida, tente novamente!')