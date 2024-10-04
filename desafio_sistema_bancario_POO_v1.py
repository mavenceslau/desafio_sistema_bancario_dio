#classe_abstrata
from abc import ABC, abstractmethod

#Classe Abstrata
class Transacao(ABC):
    
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar_conta(self, conta):
        pass

#Classes

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar_conta(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
        
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente!')
            return False
        elif valor < 0:
            print('O valor do saque deve ser maior que 0!')
            return False
        else:
            self.saldo -= valor
            return True
    
    def depositar(self, valor):
        if valor <= 0:
            print('O valor de deposito deve ser maior do que 0!')
            return False
        else:        
            self.saldo += valor
            return True
    
class Historico:
    def __init__(self):
        self._transacoes = []
    
    def transacoes(self):
        return self._transacoes
            
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.name__,
                'valor': transacao.valor    
            }            
        )

class Conta_Corrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite = 500, limite_saque = 3):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saque = limite_saque
        
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente!')
            return False
        elif valor < 0:
            print('O valor do saque deve ser maior que 0!')
            return False
        elif valor > self._limite:
            print('Limite de R$ 500.00 por saque ultrapasado.')
            return False
        else:
            self.saldo -= valor
            self._limite_saque -= 1
            return True    
        
class Pessoa_Fisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar_conta(self, conta):
        sucesso_saque = conta.sacar(self.valor)
        if sucesso_saque:
            conta.historico.adicionar_transacao(self) 
    
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar_conta(self, conta):
        sucesso_deposito = conta.depositar(self.valor)
        if sucesso_deposito:
            conta.historico.adicionar_transacao(self)     
