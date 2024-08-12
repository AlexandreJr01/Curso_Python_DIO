opcao = int
saldo = 0.0
cont_de_dep = 0
depositos = {}
saques = {}
cont_de_saq = 0
while True:
    menu_de_ops = f"""
MENU
[1] Deposito
[2] Saque
[3] Extrato
[0] Sair
    """
    print(menu_de_ops)
    opcao = int(input("Digite a opção desejada: "))
    #Opção de deposito
    if opcao == 1:
            valor_de_deposito = int(input("Digite valor a ser depositado: R$ "))
            if valor_de_deposito <= 0:
                print("Valo Inválido")
            else:
                saldo += float(valor_de_deposito)
                depositos[cont_de_dep]= f"R$ {valor_de_deposito},00"
                cont_de_dep += 1
                print("Valor depositado com sucesso!")
    #Opção de saque
    if opcao == 2:
        while True:
            valor_de_saque = int(input("Digite valor a ser sacado: R$ "))
            if cont_de_saq == 3:
                print("Número de saques excedido")
                break
            if valor_de_saque <= 0:
                print("Valor Inválido")
            else:
                if valor_de_saque > saldo:
                    print("Saldo insuficiente")
                    break
                else:
                    saldo -= float(valor_de_saque)
                    saques[cont_de_saq] = f"R$ {valor_de_saque},00"
                    cont_de_saq += 1
                    print("Saque realizado com sucesso")
                    break
    #Opção de extrato
    if opcao == 3:
        print("Extrato")
        for i in range(0,cont_de_dep):
                print(f"Despoito[{i+1}]: {depositos[i]}")
        for i in range(0,cont_de_saq):
                print(f"Saque[{i+1}]: {saques[i]}")
        print(f"Saldo: R$ {saldo:.2f}")    
    #Encerrar programa                
    if opcao ==0:
        break
