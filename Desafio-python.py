menu = """"
[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair 
"""

saldo = 0
limite = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        dep = float(input("Informe o valor que deseja depositar: "))

        if dep > 0:
            saldo += dep
            extrato += f"Deposito de: R$ {dep:.2f}"
        else:
            print("Operação invalida. Você não pode depositar valores negativos!")

        
    elif opcao == "s":
        print("Sacar")        
        saque = float(input("Informe o valor que deseja sacar: "))

        saldo_exedido = saque > saldo

        limite_exedido = saque > limite

        saque_exedido = numero_saque >= LIMITE_SAQUE

        if saldo_exedido:
            print("Saldo insuficiente!")
        
        elif limite_exedido:
            print("Operação falhou. Pois é maior que o limite diário!")
        
        elif saque_exedido:
            print("Você exedeu o limite máximo de saques!")
        
        elif saque > 0:
            saldo -= saque
            extrato += f" Saque: R$ {saque:.2f}"
            numero_saque += 1
        
        else:
            print("Operação Invalida")

    elif opcao == "e":
        print("===============Extrato=============")
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"Saldo: {saldo:.2f}")
        print("===================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")

