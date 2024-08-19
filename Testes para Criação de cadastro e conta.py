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

banco_de_usuarios = []

while True:
    msg_menu = """
    [1] Cadastro
    [2] Mostrar Banco de usuarios
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
    if opcao == 0:
        print("Programa encerrado")
        break
