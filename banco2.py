#######-VARIÁVEIS-########
saldo = 0
extrato = ""
limite_valor = 500
limite_quantidade = 3
usuarios = []
contas = []

########-FUNÇÕES-#########
def mostrar_menu():
    menu = """
==========================================
=== ESCOLHA QUE OPERAÇÃO DESEJA FAZER ====

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nu] Cadastrar novo usuário
[nc] Cadastrar nova conta
==========================================
=> """
    return menu

def deposito(valor, extrato, /):
    global saldo
    if valor > 0:
        saldo += valor
        print(f"\nO valor de R$ {valor:.2f} foi depositado com sucesso!")
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        print("\nValor inválido.")
        return saldo, extrato

def saque(*, valor, saldo, extrato, limite_quantidade):
    global limite_valor
    if valor > saldo:
        print("\nSaldo insuficiente.")

    elif valor > limite_valor:
        print(f"\nA solicitação excede seu limite de saque de {limite_valor}.")

    elif valor > 0:
        saldo -= valor
        print(f"\nO valor de R$ {valor:.2f} foi retirado com sucesso!")
        extrato += f"Saque: R$ {valor:.2f}\n"
        limite_quantidade -= 1
        return saldo, extrato, limite_quantidade

    else:
        print("\nValor inválido")

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def registrar_usuario(cpf):
    try:
        nome = input("\nNome completo: ")
        data_nascimento = input("\nData de nascimento: ")
        endereco = input("\nEndereço: ")
        novo_usuario = {"Nome": nome, "Data de Nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco}
        return novo_usuario
    except:
        print("\nOcorreu um erro")


def registrar_conta(cpf):
    try:
        id_conta = gerar_id_conta()
        nova_conta = {"CPF do Titular": cpf, "Agência": "001", "Número da Conta": id_conta}
        return nova_conta
    except:
        print("\nOcorreu um erro")

def verificar_cpf(cpf):
    global usuarios
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            return True
    return False

def gerar_id_conta():
    global contas
    novo_id = len(contas) +1
    return novo_id

def main():
    global saldo
    global extrato
    global limite_quantidade
    while True:
        opcao = input(mostrar_menu())
        if opcao.lower() == "d":
            try:
                valor_deposito = float(input("\nInforme o valor a depositar: "))
                saldo, extrato = deposito(valor_deposito, extrato)
            except Exception as e:
                print(f"\nOcorreu um erro: {type(e).__name__}. Por favor, tente novamente")

        elif opcao.lower() == "s":
            try:
                if limite_quantidade == 0:
                    print("\nJá atingiu seu limite diário de saques")
                else:
                    valor_saque = float(input("\nInforme o valor a sacar: "))
                    saldo, extrato, limite_quantidade = saque(valor = valor_saque, saldo = saldo, extrato = extrato, limite_quantidade = limite_quantidade)
            except Exception as e:
                print(f"\nOcorreu um erro: {type(e).__name__}. Por favor, tente novamente")
        
        elif opcao.lower() == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao.lower() == "nu":
            try:
                print("""
==========================================
=========== CRIAR NOVO USUÁRIO ===========\n """)
                cpf = int(input("\nInforme o CPF (somente números): "))
                if verificar_cpf(cpf) == True:
                    print("\nCPF já cadastrado!")
                else:
                    usuarios.append(registrar_usuario(cpf))
                    print(usuarios)
            except:
                print("\nCPF inválido!")

        elif opcao.lower() == "nc":
            try:
                print("""
==========================================
============ CRIAR NOVA CONTA ============\n """)
                cpf = int(input("\nInforme o CPF do titular (somente números): "))
                if verificar_cpf(cpf) == True:
                    contas.append(registrar_conta(cpf))
                    print(contas)
                else:
                    print("\nUsuário não cadastrado!")
            except:
                print("\nCPF inválido!")     
        elif opcao.lower() == "q":
            break

        else:
            print("\nOperação inválida. Por favor, selecione novamente a operação desejada.")

############-RUN-##############
main()
