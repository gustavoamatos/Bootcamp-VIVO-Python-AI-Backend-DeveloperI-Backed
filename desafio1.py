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
limiteSaque = 3
extrato = "Extrato: \n"
movimentacao = "{} - R$ {:.2f} \n"

continuar = True

while continuar:
    opcao = input(menu)
    print("-" * 100)
    if opcao == "1":
        print(selecao.format("1 - Depositar"))

        valorDeposito = float(input("Informe o valor de depósito: R$ "))

        if valorDeposito > 0:
            saldo = saldo + valorDeposito
            extrato = extrato + movimentacao.format("Depósito", valorDeposito)
            print("Depósito de R${:.2f} realizado com sucesso. Novo saldo: R${:.2f}".format(valorDeposito, saldo))
            print("-" * 100)

            sessao = input(novaOperacao).upper()
            if sessao == "S":
                continuar = True
                print("-" * 100)
            else:
                continuar = False
                print("Sessão finalizada.")
        else:
            print("Valor de depósito inválido.")
    elif opcao == "2":
         print(selecao.format("2 - Sacar"))
         print(" ")
         if limiteSaque == 0:
             print("Limite de saques diário atingido, tente novamente amanhã.")
         else:
             print("Saldo disponível: R${:.2f}".format(saldo))

             valorSaque = float(input("Informe o valor de saque: R$ "))
             print(" ")

             if valorSaque > 500 or valorSaque > saldo:
                 print("Valor de saque excede o limite de R$ 500 ou o saldo disponível, tente um valor menor.")
             else:
                 saldo = saldo - valorSaque
                 extrato = extrato + movimentacao.format("Saque", valorSaque)
                 limiteSaque = limiteSaque - 1
                 print("Saque de R${:.2f} realizado com sucesso. Novo saldo: R${:.2f}".format(valorSaque, saldo))
                 print("-" * 100)

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
         print(extrato)
         print("Saldo: R$ {:.2f}".format(saldo))
         print("-" * 100)

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