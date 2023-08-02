import time
import os

def imprime_menu():
    print(f"""
._____________________________.
|                             |
|-_-_-_-_-_$_CODEX_$_-_-_-_-_-|
|             -$-             |         
|-_-_-_-_-_$_BANKS_$_-_-_-_-_-|
|_____________________________|
|                             |
| [1] Depositar               |
| [2] Sacar                   |
| [3] Extrato                 |
| [0] Sair                    |
|_____________________________|
          """)
    
def imprime_extrato(extrato, saldo, limite):
     print(f"""
._____________________________.
|                             |
|-_-_-_-_-_$_CODEX_$_-_-_-_-_-|
|             -$-             |         
|-_-_-_-_-_$_BANKS_$_-_-_-_-_-|
|_____________________________|
          """)
     for operacao in extrato:
         print(f"""
 {operacao[0]} _____ R$ {operacao[1]:.2f}""")
     
     print(f"""      
 Saldo em conta: R$ {saldo:.2f}
 Limite: R$ {limite:.2f}
|_____________________________|
           """)

    
saldo = 0
limite = 500
extrato = [] 
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    
    imprime_menu()

    operacao = int(input("Digite o número da operação que deseja realizar: "))

    if operacao == 1:
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        if valor_deposito > 0:
            saldo+=valor_deposito
            extrato.append(["Depósito", valor_deposito])
            print(f"Valor (+{valor_deposito}) depositado com sucesso!!!")
        else:
            print("Deposite um valor maior que 0")

    elif operacao ==2:
         valor_saque = float(input("Digite o valor que deseja sacar: "))
         if numero_saques<3:
             if valor_saque <=500 and valor_saque> 0:
                if saldo - valor_saque >=0:
                    saldo-=valor_saque
                    extrato.append(["Saque", valor_saque])
                    print(f"Valor (-{valor_saque}) sacado com sucesso!!!")
                elif (saldo+limite) - valor_saque >=0:
                    limite -= valor_saque - saldo
                    saldo = 0
                    extrato.append(["Saque", valor_saque])
                    print(f"Valor (-{valor_saque}) sacado com sucesso utilizando o limite!!!")
                else:
                    print("Saque não permitido, tente outro valor!")
             else:
                 print("O valor do saque não é permitido!")
         else:
             print("Limite de saque diário atingido!")
    elif operacao==3:
        imprime_extrato(extrato, saldo, limite)
        os.system('pause')
    else:
        break

    time.sleep(2)
    os.system('cls')

