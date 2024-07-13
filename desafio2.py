menu = '''
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Criar Usuário
    5 - Criar Conta Corrente
    6 - Sair
    
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

def sacar(*, limite_saques, valor, saldo, extrato, ):
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

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario[cpf] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("O CPF informado já está sendo utilizado.")
        return

    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (no formato: dd/mm/aaaa):")
    endereco = input("Informe o endereço (no formato: Logradouro, Num - Bairro - Cidade/Sigla do estado):")

    usuarios.append({"nome:": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco})
    print("Cadastro realizado com sucesso!")

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta corrente criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} 
    print("Usuário não encontrado, tente criar a conta com um usuário válido.")
    return None

def continuar_sessao(sessao, continuar):
    if sessao == "S":
        continuar = True
        print("-" * 100)
    else:
        continuar = False
        print("Sessão finalizada.")
    return continuar

while continuar:
    opcao = input(menu)
    print("-" * 100)
    if opcao == "1":
        print(selecao.format("1 - Depositar"))

        valorDeposito = float(input("Informe o valor de depósito: R$ "))
        
        saldo, extrato = depositar(saldo, valorDeposito, extrato)

        sessao = input(novaOperacao).upper()
        continuar = continuar_sessao(sessao, continuar)
    elif opcao == "2":
        print(selecao.format("2 - Sacar"))
        print("") 

        valorSaque = float(input("Informe o valor de saque: R$ "))
        saldo, extrato, saques_disponiveis = sacar(limite_saques = saques_disponiveis, valor = valorSaque, saldo = saldo, extrato = extrato)

        sessao = input(novaOperacao).upper()
        continuar = continuar_sessao(sessao, continuar)
    elif opcao == "3":
        print(selecao.format("3 - Extrato"))
        print("")

        listar_extrato(saldo, extrato = extrato)

        sessao = input(novaOperacao).upper()
        continuar = continuar_sessao(sessao, continuar)
    elif opcao == "4":
        print(selecao.format("4 - Criar Usuário"))
        criar_usuario(usuarios)
    elif opcao == "5":
        print(selecao.format("5 - Criar Conta Corrente"))
        numero_conta = len(contas_correntes) + 1
        conta = criar_conta_corrente(agencia, numero_conta, usuarios)

        if conta:
            contas_correntes.append(conta)
    elif opcao == "6":
        print(selecao.format("6 - Sair"))
        print("Sessão finalizada.")
        break
    else:
        print("Opção inválida, informe novamente.")