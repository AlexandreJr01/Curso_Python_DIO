def depositos(valor, saldo,extrato,/,):#valor e saldo
        if  valor <= 0:
            print("Valor Inválido")
        else:
            saldo += float(valor)
            extrato[0].append(f"R$ {valor_de_deposito}")
            print("Valor depositado com sucesso!")
        return saldo , extrato

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

def extratos(saldo,/,*, extrato):
        print("Extrato")
        for i in  range(len(extrato[0])):
                print(f"Despoito[{i+1}]: {extrato[0][i]}")
        for i in range(len(extrato[1])):
                print(f"Saque[{i+1}]: {extrato[1][i]}")
        print(f"Saldo: R$ {saldo}")

opcao = int
Saldo = 0.0
Extrato = [[],[]]
Contador = 0
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
            retorno = depositos(valor_de_deposito,Saldo,Extrato)
            Saldo = retorno[0]
            extrato = retorno[1]
    #Opção de saque
    if opcao == 2:
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
    if opcao == 3:
        extratos(Saldo, extrato = Extrato)   
    #Encerrar programa                
    if opcao ==0:
        break
