
saldo = 0
numero_saque = 0
limite_saque = 3
saque_maximo = 500.00
extrato = ''

menu = f'''
###################MENU###################
APERTE:
[S] PARA SACAR;
[D] PARA DEPOSITAR
[E] PARA EXTATO
OU DIGITE OUTRA TECLA PARA SAIR DO SISTEMA
##########################################
: '''

while True:
    opcao = input(menu).upper().strip()

    if opcao == 'D':
        valor = float(input('informe o valor do deposito: '))
        if valor > 0:
            saldo += valor
            extrato+=f'Deposito: R$ {valor:.2f}\n'     
        else :
            print('Operação não realizada, valor do depositoprecisa ser maior que zero.')
    elif opcao == 'S':
        valor = float(input('informe o valor do SAQUE: '))
        if numero_saque >= limite_saque:
            print('Operação não realizada, limite diario de saque acima do permitido.')
        elif valor > saldo:
            print('Operação não realizada, valor do saque maior que saldo disponivel.')
        elif valor > saque_maximo:
            print('Operação não realizada, valor de saque acima do permitido.')
        elif valor > 0:
            saldo -= valor
            numero_saque += 1
            extrato+=f'Deposito: R$ {valor:.2f}\n'
        else:
            print('Operação não realizada, valor precisar se superior a zero.')
    elif opcao == 'E':
        print('-----EXTRATO------')
        print(extrato)
        print('------SALDO-------')
        print(saldo)
    else :
        break
    
            


