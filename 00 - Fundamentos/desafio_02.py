from datetime import datetime

"""
Desafio 02 - Sistema Bancário Simples
Este script implementa um sistema bancário simples que permite depósitos, saques e exibição de extrato.
As operações são controladas por um menu interativo e seguem regras específicas de limite e horário.
"""
saldo = 0
limite = 500
LIMITE_APOS_18H = 100 # Limite reduzido após 18h
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

"""
Sistema Bancário Simples
Este sistema permite realizar operações bancárias básicas como depósito, saque e exibição de extrato.
As operações são controladas por um menu interativo.
As regras incluem limites de saque, verificação de saldo e restrições de horário.
"""
def menu_principal():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            depositar()

        elif opcao == "s":
            sacar()

        elif opcao == "e":
            exibir_extrato()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


"""
Função para depositar valores na conta.
Atualiza o saldo e o extrato com a transação.
Se o valor for inválido, exibe uma mensagem de erro.
"""
def depositar():
    global saldo, extrato

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

""" 
Função para sacar valores da conta.
Verifica se o saldo é suficiente, se o valor está dentro do limite,
se o número de saques diários não foi excedido e se o valor é positivo.
Atualiza o saldo, o extrato e o número de saques realizados.
Exibe mensagens de erro apropriadas se as condições não forem atendidas.
"""
def sacar():
    global saldo, extrato, numero_saques

    valor = float(input("Informe o valor do saque: "))
    hora_atual = datetime.now().hour

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite or (hora_atual >= 18 and valor > LIMITE_APOS_18H):
        print(f"Operação falhou! O valor máximo para saque é de R$ {limite:.2f} até às 18h e R$ {LIMITE_APOS_18H:.2f} após esse horário.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques diários atingido.")
    elif valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

"""
Função para exibir o extrato da conta.
Mostra todas as transações realizadas e o saldo atual.
Se não houver transações, informa que não foram realizadas movimentações.
"""
def exibir_extrato():
    global saldo, extrato

    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================\n")

# Inicia o menu principal
menu_principal()