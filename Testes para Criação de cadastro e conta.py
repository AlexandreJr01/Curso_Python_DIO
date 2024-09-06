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

def criarconta(lista = [],bancocontas = []):
    lista_de_usuario = lista
    contas = bancocontas
    cpf = int(input("Digite seu CPF:"))
    for i in range(len(lista_de_usuario)):
        if cpf == lista_de_usuario[i]["CPF"]:
            num_conta = len(contas) + 1
            conta = {
            "Agência": "0001",
            "Número da Conta": num_conta,
            "CPF": cpf,
            }
            print("Conta Criada")
            contas.append(conta)
            return contas
        
        else:
            print("Usuário não cadastrado")
            return contas
    
    

banco_de_usuarios = [
    {
        "Nome": "Maria Silva",
        "CPF": 12345678901,
        "Data de nascimento": "15/05/1990",
        "Endereço": "Rua A, 100 - Centro - São Paulo"
    },
    {
        "Nome": "João Souza",
        "CPF": 23456789012,
        "Data de nascimento": "10/11/1985",
        "Endereço": "Rua B, 200 - Jardim - Rio de Janeiro"
    },
    {
        "Nome": "Ana Pereira",
        "CPF": 34567890123,
        "Data de nascimento": "25/08/1995",
        "Endereço": "Rua C, 300 - Industrial - Belo Horizonte"
    },
    {
        "Nome": "Pedro Costa",
        "CPF": 45678901234,
        "Data de nascimento": "01/01/1980",
        "Endereço": "Rua D, 400 - Centro - Salvador"
    },
    {
        "Nome": "Paula Santos",
        "CPF": 56789012345,
        "Data de nascimento": "12/12/1992",
        "Endereço": "Rua E, 500 - Bairro - Curitiba"
    }
]
banco_de_contas = []

while True:
    msg_menu = """
    [1] Cadastro
    [2] Mostrar Banco de usuarios
    [3] Criar conta
    [0] Encerrar
    """
    print(msg_menu)
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        banco_de_usuarios = cadastro(banco_de_usuarios)
    if opcao == 2:
        for i in range(len(banco_de_usuarios)):
            msg = f"""
            Nome: {banco_de_usuarios[i]["Nome"]}
            CPF: {banco_de_usuarios[i]["CPF"]}
            Data de Nacimento: {banco_de_usuarios[i]["Data de nascimento"]}
            Endereço: {banco_de_usuarios[i]["Endereço"]}
            """
            print(msg)
    
    if opcao == 3:
        banco_de_contas = criarconta(banco_de_usuarios,banco_de_contas)
        
    if opcao == 0:
        print("Programa encerrado")
        break
