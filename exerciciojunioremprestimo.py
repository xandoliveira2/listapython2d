operação = True
while operação == True: 
    print ('-'*30)
    print ('Seja bem vindo ao MyBank\n simulador de empréstimo')
    print ('-'*30)
    cliente = str(input('Já é cliente nosso? s/n: '))
    score = int(input('Digite seu serasa score: '))
    emprestimo = float(input('Digite valor desejado para empréstimo: '))
    parcelas = int(input('Quantidade de parcelas: '))
    seguro = str(input('Deseja adicionar seguro-desemprego no seu empréstimo (R$50,00)? s/n: '))
    score1 = score >= 0 and score < 300  #20%
    score2 = score >= 300 and score < 500 #15%
    score3= score >=500 and score < 700  #10%
    score4 = score >=700 and score <1001 #5%
    j3,j5,j10,j15,j20='3%','5%','10%','15%','20%'
    iof = 1.38
    if cliente.lower()=='s' and seguro.lower()=='n':
        emprestimo = (emprestimo * iof)*1.03
        valorparcelas = emprestimo / parcelas
        print ('-'*30)
        print('Resultado da simulação')
        print ('-'*30)
        print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j3,emprestimo))
    elif cliente.lower()=='s' and seguro.lower()=='s':
        emprestimo = ((emprestimo * iof) *1.03)+50
        valorparcelas = emprestimo / parcelas
        print ('-'*30)
        print('Resultado da simulação')
        print ('-'*30)
        print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j3,emprestimo))
    elif cliente.lower()=='n' and seguro.lower()=='n':
        if score1==True:
            emprestimo = (emprestimo * iof) * 1.2 +35
            valorparcelas = emprestimo / parcelas
            print('-'*30,'Resultado da simulação','-'*30)
            print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j20,emprestimo))
        elif score2==True:
            emprestimo = (emprestimo * iof) * 1.15 +35
            valorparcelas = emprestimo / parcelas
            print('-'*30,'Resultado da simulação','-'*30)
            print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j15,emprestimo))
        elif score3 == True:
            emprestimo = (emprestimo * iof) * 1.1 +35
            valorparcelas = emprestimo / parcelas
            print('-'*30,'Resultado da simulação','-'*30)
            print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j10,emprestimo))
        elif score4 == True:
            emprestimo = (emprestimo * iof)*1.05 + 35
            valorparcelas = emprestimo / parcelas
            print('-'*30,'Resultado da simulação','-'*30)
            print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j5,emprestimo))
    elif cliente.lower()=='n' and seguro.lower()=='s':
        if score1==True:
            emprestimo = (emprestimo * iof) * 1.2 + 50 + 35
            valorparcelas = emprestimo / parcelas
            print('-'*30,'Resultado da simulação','-'*30)
            print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j20,emprestimo))
        elif score2==True:
            emprestimo = (emprestimo * iof) * 1.15 + 50 + 35
            valorparcelas = emprestimo / parcelas
            print('-'*30,'Resultado da simulação','-'*30)
            print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j15,emprestimo))
        elif score3 == True:
            emprestimo = (emprestimo * iof) * 1.1 + 50 + 35
            valorparcelas = emprestimo / parcelas
            print('-'*30,'Resultado da simulação','-'*30)
            print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j10,emprestimo))
        elif score4 == True:
            emprestimo = (emprestimo * iof)*1.05 + 50 + 35
            valorparcelas = emprestimo / parcelas
            print('-'*30,'Resultado da simulação','-'*30)
            print('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros:{}\nCusto efetivo total:{} '.format(parcelas,valorparcelas,j5,emprestimo))
    denovo = str(input('Deseja realizar outra simulação? s/n:'))
    if denovo.lower()== 'n':
        print('Programa encerrado')
        operação =False
        



     
    
