def depositos_(valor, saldo,/,):#valor e saldo
        if  valor <= 0:
            print("Valo Inválido")
        else:
            saldo += float(valor)
            print("Valor depositado com sucesso!")
        return saldo

def saques_(valor, saldo ,limite):
            if valor<= 0:
                print("Valor Inválido")
            else:
                if valor_de_saque > saldo:
                    print("Saldo insuficiente")
                    break
                else:
                    saldo -= float(valor_de_saque)
                    saques.append(f"R$ {valor_de_saque},00")
                    cont_de_saq += 1
                    print("Saque realizado com sucesso")
                    break
            return saldo    

opcao = int
saldo = 0.0
depositos = []
saques = []
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
            saldo = depositos_(valor_de_deposito,saldo)
            depositos.append(f"R$ {valor_de_deposito}")
    #Opção de saque
    if opcao == 2:
        while True:
            if cont_de_saq == 3:
                print("Número de saques excedido")
                break
            valor_de_saque = int(input("Digite valor a ser sacado: R$ "))
            if valor_de_saque <= 0:
                print("Valor Inválido")
            else:
                if valor_de_saque > saldo:
                    print("Saldo insuficiente")
                    break
                else:
                    saldo -= float(valor_de_saque)
                    saques.append(f"R$ {valor_de_saque},00")
                    cont_de_saq += 1
                    print("Saque realizado com sucesso")
                    break
    #Opção de extrato
    if opcao == 3:
        print("Extrato")
        for i in  range(len(depositos)):
                print(f"Despoito[{i+1}]: {depositos[i]}")
        for i in range(len(saques)):
                print(f"Saque[{i+1}]: {saques[i]}")
        print(f"Saldo: R$ {saldo:.2f}")    
    #Encerrar programa                
    if opcao ==0:
        break