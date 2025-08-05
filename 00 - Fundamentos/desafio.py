from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
LIMITE_APOS_18H = 100 # Limite reduzido após 18h
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        horario_inseguro = datetime.now().hour >= 18

        excedeu_saldo = valor > saldo

        # Define o limite de saque dependendo do horário
        if horario_inseguro:
            limite_seguro = LIMITE_APOS_18H
        else:
            limite_seguro = limite

        excedeu_limite = valor > limite_seguro

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            if horario_inseguro:
                print(f"Operação falhou! O valor do saque excede o limite após as 18h de {LIMITE_APOS_18H:.2f}.")
            else:
                print(f"Operação falhou! O valor do saque excede o limite de {limite_seguro:.2f}.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
