menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = []
extrato_temp = ""
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0
valor_saque = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito > 0:
            saldo += deposito
            print(f"Saldo atual: R${saldo:.2f}")
            extrato_temp = f"Depósito: R${saldo:.2f}"
            extrato.append(extrato_temp)
        else:
            print("Valor do depósito inválido.")

    elif opcao == "s":
        print("Saque")
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque > 0:
                if (valor_saque <= 500):
                    if saldo >= valor_saque:
                        saldo -= valor_saque
                        numero_saques += 1
                        print(f"Saque realizado com sucesso! Saldo atual: R${saldo:.2f}")
                        extrato_temp = f"Saque: R${valor_saque:.2f}"
                        extrato.append(extrato_temp)
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("Valor do saque excede o limite de R$500,00.")
            else:
                print("Valor do saque inválido.")
        else:
            print("Você atingiu o limite de saques diários.")

    elif opcao == "e":
        print("Extrato")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Saldo atual da conta: R${saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")