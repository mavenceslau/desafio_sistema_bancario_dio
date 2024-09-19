
#Variáveis

saldo = 0
limite_saque = 3
lista_saque = []
lista_depositos = []
boas_vindas = '''
Bem vindo ao sistema bancário!               
Selecione a operação desejada:
             
    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Sair
'''
despedida = '''
Obrigado!
Finalizando acesso ao aplicativo.
'''


while True:
    try:
        menu = int(input(boas_vindas))
        
        match menu:
            case 1:    
                valor = float(input('Digite o valor a ser depositado: '))
                if valor <= 0:
                    print('O valor de deposito deve ser maior do que 0!')
                else:    
                    saldo += valor
                    lista_depositos.append(valor)
                    print(f'Deposito de R$ {valor:.2f} efetuado com sucesso.')
            case 2:
                if limite_saque == 0:
                     print('Limite de 3 saques diários alcançado.')
                else:     
                    saque = float(input('Digite o valor desejado de saque:'))
                    if saque > saldo:
                        print('Saldo insuficiente!')
                    elif saque < 0:
                        print('O valor do saque deve ser maior que 0!')    
                    elif saque > 500:
                        print('Limite de R$ 500.00 por saque ultrapasado.')
                    else:
                        saldo -= saque
                        lista_saque.append(saque)
                        limite_saque -= 1
                        print(f'Saque de R$ {saque:.2f} efetuado com sucesso.')
            case 3:
                if saldo == 0 and lista_depositos == [] and lista_saque == []:
                    print('Não houve movimentação na conta.')
                else:
                    print('Lista de depositos:')
                    for deposito in lista_depositos:
                        print(f'R$ {deposito:.2f}')
                    print('')
                    print('Lista de saques:')
                    if lista_saque == []:
                        print('Não foram efetuados saques na conta.')
                    else:
                        for saques in lista_saque:
                            print(f'R$ {saques:.2f}')
                    print('')
                    print(f'Seu saldo é de R$ {saldo:.2f}')    
            case 4:
                print(despedida)
                exit()
            case _:
                print('Operação inválida, tente novamente.')    
    except ValueError:
        print('Digite um numero entre 1 e 4.') 
        
