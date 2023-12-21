cont = 0
maior = 0
while cont <= 6 :
    cont += 1
    num = float(input("Digite um numero: "))
    if num > maior :
        maior = num
print ('O maior número é:',maior)