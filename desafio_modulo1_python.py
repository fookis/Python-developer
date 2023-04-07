menu = """
============================
==========SidBank===========

[s] Saque
[d] Deposito
[e] Extrato
[q] Sair

============================
============================
"""
saldo = 1000
saque = 0
valor_deposito = 0 
valor_limite_saque = 500
limite_saque = 0
LIMITE_SAQUES = 3
extrato = []

while True:
    opcao = input(menu)
    
    if opcao == "s":
        saque = int(input(f"""
Saque Selecionado!
*Quantidade de saques disponiveis: {LIMITE_SAQUES-limite_saque}*
Saldo disponivel: {int(saldo)}
        
Insira o valor que deseja sacar: """))
        if limite_saque < LIMITE_SAQUES:
            if saque > 0:
                if saque <= 500:
                    if saque <= saldo:
                        saldo -= saque
                        limite_saque += 1
                        print(f"""Saque realizado com sucesso!
Saldo atual: {saldo}""")
                        extrato.append(f"Saque de R${float(saque):2}")
                    else:
                        print("Valor de saque inválido! Saldo insuficiente.")
                else: 
                    print("Valor de saque inválido! O limite de saque é de R$ 500,00")
            else: 
                print("Valor de saque inválido! Insira um valor positivo")
        else:
            print("Limite de saques diários atingido.")
        
    elif opcao == "d":
        valor_deposito = int(input("""Deposito Selecionado! 
Insira o valor que será depositado: """))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Deposito realizado com sucesso!\nSaldo atual: {saldo}")
            extrato.append(f"Deposito de R${float(valor_deposito):2}")
        else:
            print("Deposito não realizado. Deposite um valor válido.")
        
    elif opcao == "e":
        if len(extrato)>0:
            print(f"Extrato:\n{extrato}")
        else:
            print("Não foram realizadas movimentações")
    elif opcao == "q":
        print("Obrigado por utilizar o SidBank!")
        break
    else:
        print("Opção inválida, por favor selecione uma das opções listadas.")    
