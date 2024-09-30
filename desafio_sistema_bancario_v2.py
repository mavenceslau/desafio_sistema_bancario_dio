#Variáveis

saldo = 0
limite_saque = 3
lista_saque = []
lista_depositos = []
lista_clientes = {}
lista_contas = {}
AGENCIA = '0001'
conta = 1
boas_vindas = '''
Bem vindo ao sistema bancário!               
Selecione a operação desejada:
     
    [1] Criar usuário       
    [2] Criar conta        
    [3] Deposito
    [4] Saque
    [5] Extrato
    [6] Listar clientes
    [7] Listar contas
    [8] Sair
'''
despedida = '''
Obrigado!
Finalizando acesso ao aplicativo.
'''
#funções
def deposito(valor, /):    
    if valor <= 0:
        print('O valor de deposito deve ser maior do que 0!')
    else:
        global saldo, lista_depositos
        
        saldo += valor
        lista_depositos.append(valor)
        print(f'Deposito de R$ {valor:.2f} efetuado com sucesso.')
        
def saque(*, valor):
    global saldo, limite_saque, lista_saque
     
    if valor > saldo:
        print('Saldo insuficiente!')
    elif valor < 0:
        print('O valor do saque deve ser maior que 0!')    
    elif valor > 500:
        print('Limite de R$ 500.00 por saque ultrapasado.')
    else:
        saldo -= valor
        lista_saque.append(valor)
        limite_saque -= 1
        print(f'Saque de R$ {valor:.2f} efetuado com sucesso.')
          
def extrato(saldo, /, lista_saque, lista_depositos):
        
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
    
def sair():
    print(despedida)
    exit()
    
def criar_conta():
    global AGENCIA, conta, lista_contas, lista_clientes
    
    cpf = input('Digite seu CPF:')
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    if cpf_numeros not in str(lista_clientes.keys()):
        print('Você deve cadastrar um usuario antes de criar uma conta!')
    else:
        usuario = lista_clientes[cpf_numeros]['nome']
        cadastro = {conta: {'Agencia': AGENCIA, 'cpf': cpf_numeros, 'Usuário': usuario}}
        lista_contas.update(cadastro)
        conta += 1
        print('Conta criada com sucesso!')

def criar_usuario():
    global lista_clientes
    
    cpf = input('Digite seu CPF:')
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    if cpf_numeros in str(lista_clientes.keys()):
        print('CPF já está cadastrado!')
    else:        
        nome = input('Digite seu nome:')
        data_nascimento = input('Digite sua data de nascimento(Ex: 25/05/1987):')
        endereco = input('Digite o endereço(Rua, numero - bairro - cidade/estado(sigla) ):')

        cadastro = {cpf_numeros: {'nome': nome, 'data nascimento': data_nascimento, 'endereço': endereco}}
        lista_clientes.update(cadastro)
        
def listar_clientes(clientes):
    global lista_clientes
    
    if lista_clientes == {}:
        print('Não há clientes cadastrados!')
    else:    
        for cliente, valor in clientes.items():
            print(f'CPF: {cliente}, Dados: {valor}')

def listar_contas(contas):
    global lista_contas
    
    if lista_contas == {}:
        print('Não há contas cadastradas!')
    else:
        for conta, valor in contas.items():
            print(f'Conta: {conta}, Dados: {valor}')                
        
#Sistema Bancário
while True:
    try:
        menu = int(input(boas_vindas))
        
        match menu:
            case 1:
                criar_usuario()    
            case 2:
                criar_conta()    
            case 3:
                valor = float(input('Digite o valor a ser depositado: '))    
                deposito(valor)
                
            case 4:
                if limite_saque == 0:
                     print('Limite de 3 saques diários alcançado.')
                else:
                    valor = float(input('Digite o valor desejado de saque:'))
                    saque(valor)
                              
            case 5:
                extrato(saldo, lista_saque = lista_saque, lista_depositos = lista_depositos)
                
            case 6:
                listar_clientes(lista_clientes)
            case 7:
                listar_contas(lista_contas)    
            case 8:
                sair()    
            case _:
                print('Operação inválida, tente novamente.')    
    except ValueError:
        print('Digite um numero entre 1 e 7.')