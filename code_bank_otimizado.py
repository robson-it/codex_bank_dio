import time
import os


####################################### FUNÇÕES ###############################################
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
| [4] Novo cliente            |
| [5] Nova conta              |
| [6] Listar contas           |          
| [0] Sair                    |
|_____________________________|
          """)
#==============================================================================================   

def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo+=valor
        extrato.append(["Depósito", valor_deposito])
        print(f"$_-_-Valor (+{valor_deposito}) depositado com sucesso!!!-_-_$")
    else:
        print("$_-_-Deposite um valor maior que 0 !-_-_$")
    
    return saldo, extrato


def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    if numero_saques < limite_saques:
        if valor <=500 and valor> 0:
            if saldo - valor >=0:
                saldo-=valor
                extrato.append(["Saque", valor])
                print(f"$_-_-Valor (-{valor}) sacado com sucesso!!!-_-_$")
            elif (saldo+limite) - valor >=0:
                limite -= valor - saldo
                saldo = 0
                extrato.append(["Saque", valor])
                print(f"$_-_-Valor (-{valor}) sacado com sucesso utilizando o limite!!!-_-_$")
            else:
                print("$_-_-Saque não permitido, tente outro valor!-_-_$")
        else:
            print("$_-_-O valor do saque não é permitido!-_-_$")
    else:
        print("$_-_-Limite de saque diário atingido!-_-_$")

    return saldo, extrato
#==============================================================================================  

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
#==============================================================================================     

def novo_cliente (clientes):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_clientes(cpf, clientes)

    if usuario:
        print("\n$_-_-Já existe cliente com esse CPF!-_-_$")
        return

    nome = input("Informe o nome completo do cliente: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("$_-_-Novo cliente cadastrado com sucesso!-_-_$")
#============================================================================================== 

def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if clientes["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
#============================================================================================== 


def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do usuário: ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("\n$_-_-Conta criada com sucesso!-_-_$")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\n$_-_-Cliente não encontrado, a conta não pode ser criada!-_-_$")
#============================================================================================== 


def listar_contas(contas):
    
    for conta in contas:
        linha = f"""._____________________________.
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
    print(f"""
._____________________________.
|                             |
|-_-_-_-_-_$_CODEX_$_-_-_-_-_-|
|             -$-             |         
|-_-_-_-_-_$_BANKS_$_-_-_-_-_-|
|_____________________________|
          """)
    print(linha)
    print("|_____________________________|")
#============================================================================================== 

####################################### FIM FUNÇÕES #######################################

####################################### CONSTANTES ########################################
LIMITE_SAQUES = 3
AGENCIA = "0001" 
####################################### FIM CONSTANTES ####################################

####################################### VARIÁVEIS #########################################
saldo = 0
limite = 500
extrato = [] 
numero_saques = 0
clientes=[]
contas=[]
####################################### FIM VARIÁVEIS #####################################

####################################### FUNÇÃO PRINCIPAL ##################################
def main():
    while True:

        
        imprime_menu()

        #RECEBE O NÚMERO DA OPERAÇÃO
        operacao = int(input("Digite o número da operação que deseja realizar: "))

        #DEPOSITAR
        if operacao == 1:
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = depositar (saldo, valor_deposito, extrato)

        #SACAR    
        elif operacao ==2:
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor_saque,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
            )

        #IMPRIMIR EXTRATO
        elif operacao==3:
            imprime_extrato(extrato, saldo, limite)
            os.system('pause')

        #CADASTRAR CLIENTE
        elif operacao==4:
            novo_cliente(clientes)

        #CADASTRAR NOVA CONTA
        elif operacao==5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)

        #EXIBIR TODAS AS CONTAS CADASTRADAS
        elif operacao==6:
            listar_contas(contas)
        
        #SAIR
        elif operacao==0:
            break

        #OPÇÃO INVÁLIDA
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

        time.sleep(2)
        os.system('cls')
####################################### FIM FUNÇÃO PRINCIPAL ###############################

main()

