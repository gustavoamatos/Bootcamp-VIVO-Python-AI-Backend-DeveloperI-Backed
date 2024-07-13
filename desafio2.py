menu = '''
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair
    
    Escolha uma opção:
'''

novaOperacao = '''
    Você deseja fazer uma nova operação?
    
    S para Sim
    Qualquer tecla para Não
    
    Escolha uma opção:
'''

selecao = "Opção selecionada: {}"

saldo = 0
valorLimiteSaque = 500
saques_disponiveis = 3
extrato = "Extrato: \n"
movimentacao = "{} - R$ {:.2f} \n"
agencia = "0001"

continuar = True

''''''
usuarios = []

contas_correntes = []

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Valor de depósito inválido.")
    else:
        saldo += saldo + valor
        extrato += movimentacao.format("Depósito", valor)
        print("Depósito de R${:.2f} realizado com sucesso. Novo saldo: R${:.2f}".format(valor, saldo))
        print("-" * 100)
        
    return saldo, extrato

def sacar(*, limite_saques, valor_limite, valor, saldo, extrato, ):
    if limite_saques == 0:
        print("Limite de saques diário atingido, tente novamente amanhã.")
    else:
        print("Saldo disponível: R${:.2f}".format(saldo))

        if valor > 500 or valor > saldo:
            print("Valor de saque excede o limite de R$ 500 ou o saldo disponível, tente um valor menor.")
        else:
            saldo -= valor
            extrato += movimentacao.format("Saque", valor)
            limite_saques -= 1
            print("Saque de R${:.2f} realizado com sucesso. Novo saldo: R${:.2f}".format(valor, saldo))
            print("-" * 100)

        return saldo, extrato, limite_saques

def listar_extrato(saldo, /, *, extrato):
        print(extrato)
        print("Saldo: R$ {:.2f}".format(saldo))
        print("-" * 100)

while continuar:
    opcao = input(menu)
    print("-" * 100)
    if opcao == "1":
        print(selecao.format("1 - Depositar"))

        valorDeposito = float(input("Informe o valor de depósito: R$ "))
        
        saldo, extrato = depositar(saldo, valorDeposito, extrato)

        sessao = input(novaOperacao).upper()
        if sessao == "S":
            continuar = True
            print("-" * 100)
        else:
            continuar = False
            print("Sessão finalizada.")
    elif opcao == "2":
        print(selecao.format("2 - Sacar"))
        print("") 

        valorSaque = float(input("Informe o valor de saque: R$ "))
        saldo, extrato, saques_disponiveis = sacar(limite_saques = saques_disponiveis, valor = valorSaque, saldo = saldo, extrato = extrato)

        sessao = input(novaOperacao).upper()
        if sessao == "S":
            continuar = True
            print("-" * 100)
        else:
            continuar = False
            print("Sessão finalizada.")
    elif opcao == "3":
         print(selecao.format("3 - Extrato"))
         print("")

         sessao = input(novaOperacao).upper()
         if sessao == "S":
             continuar = True
             print("-" * 100)
         else:
             continuar = False
             print("Sessão finalizada.")
    elif opcao == "4":
         print(selecao.format("4 - Sair"))
         print("Sessão finalizada.")
         break
    else:
         print("Opção inválida, informe novamente.")