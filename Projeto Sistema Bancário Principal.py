#Função de Criar Usuário
def cadastro(lista = []):
    lista_de_usuario = lista
    nome = input("Digite seu nome: ")
    cpf = int(input("Digite seu CPF: "))
    for i in range(len(lista_de_usuario)):
        if cpf == lista_de_usuario[i]["CPF"]:
            print("CPF já cadastrado")
            return lista_de_usuario
    data_de_nascimento = input("Digite sua data de nascimento: ")
    print("Endereço")
    cidade = input("Cidade: ")
    bairro = input("Bairro: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    endereço = f"{rua},{numero} -{bairro} - {cidade}."

    usuario = {
    "Nome": nome,
    "CPF": cpf,
    "Data de nascimento": data_de_nascimento,
    "Endereço": endereço,
    }
    lista_de_usuario.append(usuario)
    return lista_de_usuario
#Função de Criar Conta
def criarconta(lista = [],bancocontas = []):
    lista_de_usuario = lista
    contas = bancocontas
    cpf = int(input("Digite seu CPF:"))
    for i in range(len(lista_de_usuario)):
        if cpf == lista_de_usuario[i]["CPF"]:
            num_conta = len(contas) + 1
            conta = {
            "Agência": "0001",
            "Usuário": lista_de_usuario[i]["Nome"],
            "Número da Conta": num_conta,
            "CPF": cpf,
            }
            print("Conta Criada")
            contas.append(conta)
            return contas
    print("Usuário não cadastrado")
#Função de deposito
def depositos(valor, saldo,extrato,/,):#valor e saldo
        if  valor <= 0:
            print("Valor Inválido")
        else:
            saldo += float(valor)
            extrato[0].append(f"R$ {valor_de_deposito}")
            print("Valor depositado com sucesso!")
        return saldo , extrato
#Funçao de Saque
def saques(*,saldo,valor,extrato,contador):
        if valor <= 0:
            print("Valor Inválido")
        elif valor > saldo:
            print("Saldo Insuficiente")
        else:
            saldo -= float(valor)
            extrato[1].append(f"R$ {float(valor_de_saque)} ")
            contador += 1
        return saldo, extrato, contador
#Função de Extrato
def extratos(saldo,/,*, extrato):
        print("Extrato")
        for i in  range(len(extrato[0])):
                print(f"Despoito[{i+1}]: {extrato[0][i]}")
        for i in range(len(extrato[1])):
                print(f"Saque[{i+1}]: {extrato[1][i]}")
        print(f"Saldo: R$ {saldo}")

banco_de_contas = [
    {
        "Agência": "0001",
        "Usuário": "Maria Silva",
        "Número da Conta": 1,
        "CPF": 12345678901
    },
    {
        "Agência": "0001",
        "Usuário": "João Souza",
        "Número da Conta": 2,
        "CPF": 23456789012
    },
    {
        "Agência": "0001",
        "Usuário": "Ana Pereira",
        "Número da Conta": 3,
        "CPF": 34567890123
    },
    {
        "Agência": "0001",
        "Usuário": "Pedro Costa",
        "Número da Conta": 4,
        "CPF": 45678901234
    },
    {
        "Agência": "0001",
        "Usuário": "Paula Santos",
        "Número da Conta": 5,
        "CPF": 56789012345
    }
]

banco_de_usuarios = [
    {
        "Nome":"Maria Silva",
        "CPF":12345678901,
        "Data de nascimento": "15/05/1990",
        "Endereço": "Rua A, 100 - Centro - São Paulo"
    },
    {
        "Nome":"João Souza",
        "CPF":23456789012,
        "Data de nascimento": "10/11/1985",
        "Endereço": "Rua B, 200 - Jardim - Rio de Janeiro"
    },
    {
        "Nome":"Ana Pereira",
        "CPF": 34567890123,
        "Data de nascimento": "25/08/1995",
        "Endereço": "Rua C, 300 - Industrial - Belo Horizonte"
    },
    {
        "Nome":"Pedro Costa",
        "CPF":45678901234,
        "Data de nascimento": "01/01/1980",
        "Endereço": "Rua D, 400 - Centro - Salvador"
    },
    {
        "Nome":"Paula Santos",
        "CPF":56789012345,
        "Data de nascimento": "12/12/1992",
        "Endereço": "Rua E, 500 - Bairro - Curitiba"
    }
]

opcao = int
Saldo = 0.0
Extrato = [[],[]]
Contador = 0
while True:
    menu_de_ops = f"""
MENU
[2] Criar Usuário
[3] Mostrar Banco de Usuarios
[4] Cria Conta
[4] Mostrar Contas
[5] Deposito
[6] Saque
[7] Extrato
[0] Sair
    """
    print(menu_de_ops)
    opcao = int(input("Digite a opção desejada: "))
    
    #Opção de criar usuário
    if opcao == 1:
        banco_de_usuarios = cadastro(banco_de_usuarios)
        
    #Opção de mostrar os usuários cadastrados   
    if opcao == 2:
        for i in range(len(banco_de_usuarios)):
            msg = f"""
            Nome: {banco_de_usuarios[i]["Nome"]}
            CPF: {banco_de_usuarios[i]["CPF"]}
            Data de Nacimento: {banco_de_usuarios[i]["Data de nascimento"]}
            Endereço: {banco_de_usuarios[i]["Endereço"]}
            """
            print(msg)
            
    #Opção de criar contas
    if opcao == 3:
        banco_de_contas = criarconta(banco_de_usuarios,banco_de_contas)
    
    #Opção de contas criadas
    if opcao == 4:
        for i in range(len(banco_de_contas)):
            msg = f"""
            Agência: {banco_de_contas[i]["Agência"]}
            Número da Conta: {banco_de_contas[i]["Número da Conta"]}
            CPF: {banco_de_contas[i]["CPF"]}
            """
            
    #Opção de deposito
    if opcao == 5:
            valor_de_deposito = int(input("Digite valor a ser depositado: R$ "))
            retorno = depositos(valor_de_deposito,Saldo,Extrato)
            Saldo = retorno[0]
            extrato = retorno[1]
            
    #Opção de saque
    if opcao == 6:
            while True:
                if Contador == 3:
                    print("Limite de saques atingido")
                    break
                valor_de_saque = int(input("Digite valor de saque: R$ "))
                retorno = saques(saldo = Saldo, valor = valor_de_saque, extrato = Extrato ,contador = Contador)
                Saldo = retorno[0]
                Extrato = retorno[1]
                Contador= retorno[2]
                break
            
            
    #Opção de extrato
    if opcao == 7:
        extratos(Saldo, extrato = Extrato)   
    #Encerrar programa                
    if opcao == 0:
        break
