operação = True
while operação == True: 
    print ('-'*30)
    print ('Seja bem vindo ao MyBank\n simulador de empréstimo')
    print ('-'*30)
    cliente = str(input('Já é cliente nosso? s/n: '))
    if cliente.lower()=='n':
        score = int(input('Digite seu serasa score: '))
    emprestimo = float(input('Digite valor desejado para empréstimo: '))
    parcelas = int(input('Quantidade de parcelas: '))
    seguro = str(input('Deseja adicionar seguro-desemprego no seu empréstimo (R$50,00)? s/n: '))
    score1 = score >= 0 and score < 300  #20%
    score2 = score >= 300 and score < 500 #15%
    score3= score >=500 and score < 700  #10%
    score4 = score >=700 and score <1001 #5%
    j='3%'
    iof = 1.0038
    tarifa = 35
    if cliente.lower() == 's':
        emprestimo = emprestimo * 1.03
    elif cliente.lower()=='n' and score1 == True:
        emprestimo = (emprestimo * 1.2) + tarifa
        j = '20%'
    elif cliente.lower()=='n' and score2 == True:
        emprestimo = (emprestimo * 1.15) +tarifa
        j = '15%'
    elif cliente.lower()=='n' and score3 == True:
        emprestimo = (emprestimo * 1.1) + tarifa
        j = '10%'
    elif cliente.lower()=='n' and score4 == True:
        emprestimo = (emprestimo * 1.05) + tarifa
        j = '5%'
    if seguro.lower() == 's':
        emprestimo = emprestimo + 50
    elif seguro.lower() == 'n':
        break
    custototal = emprestimo * iof
    valorparcelas = custototal / parcelas 
    print ('-'*30,'Resultado da simulação','-'*30)
    print ('Quantidade de parcelas: {}\nValor das parcelas: {}\nTaxa de juros: {}\nCusto efetivo total: {}'.format(parcelas,valorparcelas,j,custototal))
    print ('-'*90)
    denovo = str(input('Deseja realizar outra simulação? s/n:'))
    if denovo.lower() == 'n':
        print('Programa encerrado')
        operação = False
    elif denovo.lower()=='s':
        print('Carregando sistema')
    else:
        print('Resposta não reconhecida, encerrando programa.\nPrograma encerrado')
        operacao = False