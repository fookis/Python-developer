import textwrap

def menu():
    menu ="""
    ============= SidBank =============
    [s]\tSaque
    [d]\tDeposito
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Deósito realizado com sucesso!")
    else:
        print("Operação falhou! Valor informa é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, limite, extrato, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = saldo < valor
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não possui saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excedeu o limite.")
    elif excedeu_saques:
        print("Operação falhou! Você execeu o limites de saques diários.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        print("Retire o dinheiro na boca do caixa! xD")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def obterextrato(saldo, /, *, extrato):
    print("\n============= EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================================")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf , usuarios)
    if usuario:
        print("\njá existe usuário com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (longadouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrato, tente novamente.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
            """
        print("="* 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Insira o valor de saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                limite=limite, 
                extrato=extrato,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )
        elif opcao == "e":
            obterextrato(saldo, extrato=extrato)
        elif opcao == "nu":
            novo_usuario(usuarios)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "q":
            print("Obrigado por usar o SidBank!")
            break
        else:
            print("Operação inválida, por favor seleciona novamente a operação desejada.")

main()
