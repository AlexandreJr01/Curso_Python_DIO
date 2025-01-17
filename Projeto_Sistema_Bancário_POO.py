from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
            self.endereco = endereco
            self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

#Resgistro das informações pessoas do cliente
class Registro_Cliente(Cliente):
    def __init__(self,nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

#Informações da conta Bancária dos clientes
class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
       
    @classmethod
    def criar_conta(cls, numero_conta,cliente):
        return cls(numero_conta,cliente)
       
    @property
    def saldo(self):
        return self._saldo
    
    @property   
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo = self._saldo
        if valor > saldo:
            print("Você não possui saldo suficiente")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com Sucesso")
            return True
        else:
            print("Valor Inválido")
            
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito Realizado com Sucesso")
        else:
            print("Valor Inválido")
            return False

        return True
        
class Conta_Corrente(Conta):
    def __init__(self, numero_conta, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero_conta, cliente)           
        self.limite = limite
        self.limite_saque = limite_saque
    
    def sacar(self,valor):
        numero_saques = len([transacao for transacao in self._historico.transacoes if transacao["Tipo"] == Saque.__name__])
        
        if valor > self.limite:
            print("Valor de Saque excedido")
        
        elif numero_saques >= self.limite_saque:
            print("Número máximo de saque Atingidos")
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""
        Agência: {self.agencia}
        Número da Conta: {self.numero_conta}
        Cliente: {self.cliente.nome}
        
    """


class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "Tipo": transacao.__class__.__name__,
                "Valor": transacao.valor,
                "Data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
    
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @classmethod
    def registar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def Registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def resgitrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu_administrador():
    menu = """
    ========|MENU|========
    [1]Listar Contas
    [2]Registrar Usuário
    [3]Acessar Menu de Usúario
    [0]Encerrar programa
    """
    opcao = input("Digite a opção:")
    return opcao

def filtro(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

#Verificar se existe se o usuário possui conta
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("")