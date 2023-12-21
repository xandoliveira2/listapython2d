lista = list()
inserir = ''
import os
print('COMANDOS: \n 1- Digite [ . ] para encerrar o programa \n 2- Digite [ clean ] para limpar a lista\n 3- Digite [ remove ] e depois o número inteiro sem cortes para remover o número da lista')
while inserir != '.':
    inserir = str(input('Digite o número sem abreviações e tudo junto (ex: ddd1953291245): '))
    if inserir == '.':
        pass
    elif inserir.lower() == 'clean':
        os.remove('textosobreadvertencia.txt')
        texto = open('textosobreadvertencia.txt','w')
        texto.close()
        print('Arquivo resetado, a pasta está agora totalmente vazia')
        break
    elif inserir.lower() == 'remove':
        remover = str(input('Digite o número que quer excluir:'))
        texto = open('textosobreadvertencia.txt','r+')
        for numeros in texto:
            if remover == numeros:
                texto.close()
    else:
        texto = open('textosobreadvertencia.txt','a')
        texto.write(f'{inserir}\n')
        texto.close()
texto = open('textosobreadvertencia.txt','r')
for numeros in texto.readlines():
    print (numeros)
    if lista.count(numeros) >= 3 :
        print(f'\nO número: {numeros:20}já desrespeitou 3 vezes ou mais\nExclua para continuar a verificação')
        break

texto.close()
