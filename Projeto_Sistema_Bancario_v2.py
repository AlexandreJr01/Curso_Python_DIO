def depositos_(valor, saldo,/,):#valor e saldo
        if  valor <= 0:
            print("Valo Inválido")
        else:
            saldo += float(valor)
            print("Valor depositado com sucesso!")
        return saldo

def saques_(*,saldo,valor,contador):
        saldo -= float(valor)
        contador += 1
        return saldo,contador


opcao = int
Saldo = 0.0
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
            Saldo = depositos_(valor_de_deposito,Saldo)
            depositos.append(f"R$ {valor_de_deposito}")
    #Opção de saque
    if opcao == 2:
            while True:
                valor_de_saque = int(input("Digite valor de saque: R$ "))
                if valor_de_saque <=0:
                    print("Valor Inválido")
                elif valor_de_saque > Saldo:
                    print("Saldo Insuficiente")
                    break
                else:
                    retorno = saques_(saldo = Saldo, valor = valor_de_saque,contador = cont_de_saq)
                    Saldo = retorno[0]
                    saques.append(f"R$ {float(valor_de_saque)} ")
                    cont_de_saq = retorno[1]
                    break
            
            
    #Opção de extrato
    if opcao == 3:
        print("Extrato")
        for i in  range(len(depositos)):
                print(f"Despoito[{i+1}]: {depositos[i]}")
        for i in range(len(saques)):
                print(f"Saque[{i+1}]: {saques[i]}")
        print(f"Saldo: R$ {Saldo}")    
    #Encerrar programa                
    if opcao ==0:
        break
