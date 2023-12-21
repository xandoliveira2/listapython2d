pi = 3.14159265359
oi = 2.222
numeroaleatorio=100
var = str('124.567.235-8811211') 
a= 'teste1'
b= 'teste2'
frase = 'academia girafa'
print(var.replace('.',',').replace('-','_'))#esse codigo eu explico mais p baixo, foi só para fazerum teste
print(f"pi is {var}")#definicição desse print 
##f no começo significa uma especie de formatacao que vai permitir 'ler' variáveis dentro do texto que estejam dentro de {} (chaves)
## "texto" tudo que esta dentro de aspas simples ou composta ' ou " sera string (texto) que será exibido na tela
##{} é abertura de chaves para inserir uma variavel dentro
##pi nome da variáv   
##: é uma ligacao da variavel com o que vem a seguir
##. significa que é casa decimal, ou seja pi :(dois pontos aqui interligando pi com sua casa decimal que começa no .14...) .
##5 é quantas casas depois da virgula (nesse caso né, n sei se tem outros, mas com certeza tem) vai ser mostrado 
# (com base na variavel, ou seja, nao adianta querer mostrar 10 numeros depois da virgula se sua variavel tem so 5 casas decimais)
##f é o tipo q nesse caso significa float nesse caso (quando se usar . para decimais só sera possivel usar float de qualquer maneira) mas você poderia também
#botar % no lugar do f, porém nao nesse contexto até onde eu esteja ciente agora, você pode usar quando o número já e decimal tipo 0.24 por exemplo se vc botar a = 0.24 pode botar:
#print(f"Porcentagem de:{a:.2%}") que será exibido 24.00% por conta do 2 dps do ponto, caso queira mostrar so 24 basta nao botar ou botar 
#Obs: sempre lembrar de fechar com " ou ' antes de fechar o )
print(f'texto {pi:.5}')

print('se',a,' é igual a verdadeiro,\n e,',b,' é igual a falso')
#atenção que a \ é o inverso da / q geralmente usa, prestar atencao
#\n significa uma quebra de linha ou seja, vai rodar até 'verdadeiro,' e depois no "e, ',b,'.." vai rodar na linha de baixo
#\" é para você botar aspas no texto, para q o python nao reconheça o " como fechamento
print(a+'é isso dai', )# usar + faz com que a linha continue direto exemplo 'a significa ola', ficaria olaé isso dai, teria que botar um
#espaço fazendo a+' é isso dai' ou apenas usando uma , já que a virgula é o mesmo proposito so que com o espaço já embutido
#PORÉMA GORA VOU FAZER O A VIRAR OUTRO VALOR
a = 'AGORA É ISSO DAQUI 132'
print(a,'kkk' )
#maneiras de fazer um comentario, # com uma unica linha e 
print (a.upper().isupper())#.isupper é uma pergunta praticamente, que retorna valor de verdadeiro ou falso
#.upper transforma texto em maiusculo exm: teste.upper() == 'A'
#.lower transforma texto em minusculo
#.upper e lower so funciona em str, nao funcionara em int/float/list/boolean
print(len(a)) #len vai contar quantos números tem dentro da variavel a por exemplo, quantos espaços de caracteres ocupou por exemplo
print(len(var))# len de length que é comprimento né, então faz o sentido da funcao
if len(var) > 10 and len(var) <20 :
    print("ok")
else:
    print('not okay')
print(var[6]) #ao usar [] você pode puxar por exemplo, o 6 caractere da variavel var que é o numero 7 na variavel var feita no começo do codigo
#esses itens tmb pode ser chamado de index e começa no 0, ou seja o numero por exemplo é 124.567, o index 0 é o 1, o index 1 é o 2, o index 2 é o 4
#o index 3 é o ., o index 4 é o 5 e o index 5 é o 6, e p completar o index 6 ( que é oque ta puxando no exemplo) é o 7 
#OBS: pode apenas ser usado em string
print(var.index('7')) #esse é o contrário, nesse você bota o valor que você quer saber qual número o index representa, ou seja, o número 7
#está ocupando o index 6
print(var.index('211')) #aqui ele vai me dizer onde começa o index,no caso ele reconhece o 2 como o começo, e o 2 ocupa o index numero 16 na var
print(var.index('11'))#existe dois 11 na variavel var, ele vai dizer onde começa a primeira, p especificar a segunda a gente bota a ordem de um 
#conjunto unico separado como eu fiz no exemplo 211
#OBS: PODE APENAS SEM USADO EM STRING
#OBS: se voce botar valor invalido, vai dar errado
print(frase)
print(frase.replace('girafa','elefante')) # esse comando .replace() indica que vc trocara de nome determinada 'coisa', entao nesse caso estou trocando
#girafa por elefante, lembrar das aspas e da virgula separando os dois
print(frase.replace('academia','papelaria').replace('girafa','elefante'))#Para trocar mais de um valor, lembrar de botar outro .replace no fechamento
#do parentese como no exemplo acima
#OBS: pode apenas ser usado em string (ou seja, nao vai funcionar em int/float/list/boolean)
print(b.capitalize()) #esse capitalize significa que vai imprimir a variavel b, com a primeira letra maiuscula e o resto minuscula
#OBS: denovo, apenas funciona com variaveis STRING
print(frase.__len__())
print(frase[0:3],frase[5:10],frase[0:1])#interessante observar que ele so mostrara o valor do primeiro até o anterior ao segundo
#exemplo: 0:3, ele mostrara o valor de 0 até 2  
print (10%3) #sinal de % vai voltar o número o qual sobrou dessa equação, ou seja, 10/3 da 3 e sobra 1, ele voltará o 1 que é a sobra que não pôde ser dividida inteiramente
eng =  3
print  (str(eng) + ' olá' , eng + 2)
print(eng.__abs__()) #abs retorna sempre valores positivos, não importa se é real ou inteiro/ ( em explicacao retorna o valor absoluto)
print(abs(eng)) #outra forma até mais prática e facil de fazer oque tá escrito em cima
print(pow(10,3))#indica potencia, nesse caso 10 elevado a 3 potencia
print(max(3,6,9)) # retorna o maior valor dentre os que estão dentro dos parenteses
print(min(3,6,9))# retorna o menor valor dentre os que estão dentro dos parenteses
print(round(1.49))# irá arredondar o número para o mais proximo inteiro, ex 2.7 se arredondará para 3 e 1.2 se arredondará p 1
#na funcao de cima so pode botar 1 valor aparentemente dentro do parenteses,a partir de 1.5 ele arredonda p mais e de 1.4999... para menos
from math import * # isso vai pegar da biblioteca do python mais funçoes de matematicas para usar (as abaixos serao demonstrações que são importadas com esse codigo)
print(floor(1.9)) #arredondará para o menor ao invés de maior
print(ceil(1.1)) #arredondará para o maior ao invés de menor
print(sqrt(55)) #sqrt significa square root e a traducao literal é raiz quadrada, e já da para entender oque faz, vai puxar a raiz quadrada do número
lista1=['Nomes','Carlos','Pedro', 'Juan', 'Joao', 'Alberto',2]
numerosorte = [5,13,17,18,22,24]
#lista1.extend(numerosorte)
#lista1.append(numerosorte)
#lista1.append('Yago')
#lista1.insert(3,'Gabriel') 
#lista1.remove('Nomes')
#lista1.clear()
#lista1.pop()
#print (lista1.index('Alberto'))
#lista1.sort() esse comando em lista fara com que o conteúdo seja colocando em ordem crescente
#lista1.reverse() esse comando em lista fará com que o conteúdo inverta a sua ordem (ex: antes era 1 2 10 4, ficará> 4 10 2 1)
#lista2=lista1.copy() esse comando copiara uma lista e seja identica uma a outra 
#print (lista1.count('Alberto)) contará quantas vezes Alberto aparece na lista1
#print(lista1.index('algum item da lista')) mostrará a você qual o valor index que aquele item na lista determina, por exemplo em uma lista que 
#contenha valores 1 2 3 nessa ordem por exemplo, e botar lista1.index(2) em um PRINT (importante essa condicao), vai printar o número da lista em index
#que o 2 ocupa, que nesse caso seria o valor 1, o 0 index seria o número 1 e o 2 index seria o número 3 nesse exemplo
#.pop remove o ultimo item da lista
#.clear nos dará uma lista vazia e limpa
#.remove removerá aquele determinado item da lista, porém precisa escrever exatamente qual quer remover se não dará erro, lembrar d botar aspas
#em string
#.insert permite adicionar um novo valor em qualquer lugar da lista usando parametro ( numero do index , valor a ser adicionado), e nesse caso, o
#número do index por exemplo represente 3 - juan, ele passara a ser 4 - juan e o valor a ser adicionado que ocupará o lugar 3
#.extend em lista permitira que você acrescente outra lista no final de uma
#.append em lista acrescenta novos valores sempre no final da lista
#dando run em ambos (extend e append) vc nota a diferenca que com append numerosorte fica lista dentro de lista, no extend reconhece como 1 lista só
#lista sobre lista eu falo que abre dois [[]]por exemplo

#sobre tuplas: para usar tupla você precisa botar parenteses no conteúdo
tuplas = (1,4,65432,564575)
# a principal diferença entre tuplas e listas, é que tuplas são imutáveis, ou seja, não da para modificar seu conteúdo, nem adicionar nem excluir
print (tuplas) # esse comando printará todo conteúdo da tupla
print (tuplas[3]) # esse comando puxa por index (visto ja em cima nesse texto) e você pode puxar um elemento especifico da tupla
#se botar por exemplo tuplas[1]=10 dará erro, pois como visto na primeira linha embaixo de tuplas= é que o valor NÃO PODE SER MODIFICADO
#dá p criar lista com várias tuplas
tuplateste = [(1,23,4),(532,421,567),('LEROY')]
print (tuplateste)
print (tuplateste[1])
#sobre funçoes
def dizoi ():
    print ('Olá')
dizoi()
#apenas botar o nome da função já chamará ela e ela será executada, se certa forma o python le que é p puxar a funcao dizoi que está na linha do def
#na linha 120 por ex.
#sempre bom nomar funcoes apenas com letras minusculas
#o parenteses () significa parametro, por exemplo, para que seja executado dizoi, precisa de parametros A e B por exemplo:
x = 20
y = -9
def matbas(x,y):#obs: não esquecer dos :
    print(x + y)
matbas(x,y)
#def estamos falando para definir que nesse caso o nome dizoi(esse nome pode ser qualquer um, é como criar variável), vai fazer a funcao que está
# depois dos parenteses e do dois : ,  precisamos identar tudo que foi para baixo agora, se não identarmos (dar o espaço do começo da linha onde
# começa o def) será considerado fora do def e pode ocasionar algum erro   
#return:
def cube(x): #apenas esse código não dá nada, fica um print vazio, é para isso que usaremos o return
    x*x*x
cube(x)
def cube(x): 
   return x*x*x # praticamente diz para voltar a funcao x*x*x para printar na tela(também podemos definir qual tipo de dado deve retornar,ex: return int(x*x*x) )
   print('olá') # esse comando não será executado, porque o python só le até o return, é como se fosse um ponto final, claro que tem suas excessoes
   #que veremos mais p frente, porém por enquanto return tem funcao final doq print, se quiser printar algo bote emcima do return,porque depois
   #que ler o return a funcao nao pega mais linhas e volta para onde está executando no codigo
   #unico que poderá escrever depois do return é se você já tiver escrito uma declaracao de condicao, IF, ai poderá ter mais de um return
   #ex: if x*x*x = y    return y//elif x*x*x = z  return z...
print(cube(x))
#podemos também atribuir outros valores para funcoes puxar sem que tenhamos que alterar, como por exemplo:
resultad = cube(5.2)
print (resultad) #esse comando vai mostrar na tela resultad que é a funcao cube com numero 5, ou seja 5*5*5 que é 125

#declaração if (statement if)
#textinho exemplo
# hoje acordei as 7 para ir para escola
# SE eu estiver com fome:                    #se essa condição for verdadeira
#     como café da manha                     # vai executar esse comando
#                                            #se não
#Antes de sair de casa, olho para o céu      #pulará para esse
#   SE tiver com nuvens:                     #o mesmo acontece aqui, se isso for verdadeiro
#       levo meu guardachuva                 #vai acontecer isso,
#   caso contrário:                          # se não
#       levo oculos de sol                   #isso
#if statement so funciona com valores booleanos, ou seja, verdadeiro ou falso
Homem = True                                 # aqui declaramos que Homem recebeu valor verdadeiro
if Homem == True:                            #aqui dizemos, se homem for verdadeiro :
    print('Genêro masculino')                # exiba na tela genero masculino
else:                                        # caso contrario
    print('Genêro feminino')                 # exiba genero feminino              
#em if statement, é necessário fazer identação que nem em funções, ou seja, tudo que tiver identado no if é o que será executado
vdd3=False
vdd1=True
vdd2=False
if vdd1 or vdd2: # esse comando or, ele faz com que desde que 1 comparação seja verdadeira, vai voltar verdadeiro para o python
    print ('olá')                 #ou seja, mesmo que a condicao vdd2==false seja falsa, o primeiro é vdd, e como tem 1 verdadeiro, o valor volta 
else:                             # verdadeiro
    print('tchau')
if vdd1  and vdd2 : # com o comando and, só sera verdadeiro se todas setenças de comparações forem verdadeiras
    print ('olá')                   
elif vdd1 and not (vdd2) and vdd1 and not (vdd3):         # not usa quando vc quer valor falso ou contrário, nesse caso é como se eu perguntasse:
    print('ok')                   # se vdd1 for verdadeiro  e se vdd2 NÃO for verdadeiro: mostre na tela ok
else:                             # E se vdd1 for verdadeiro e vdd3 NAO for vdd: mostre ok, ou seja, ele tem 2 condicoes, vdd1 e notvdd2, e vdd1 e notvdd3
    print('tchau')                # esses parenteses serve para negar tudo que tiver dentro do parenteses usando o not  

def numerosabc (x,y,z):
    r = x+y+z
    print (r)
numerosabc (1,14,7)

def numerosmaiores (a,b,c,d): #nesse caso ele vai printar o valor se seguir as condições do if
    if a>b and a>c and a>d:
        print(a) 
    elif b>c and b>d:
        print(b)
    elif c>d:
        print(c) 
    else:
        print(d)
    
numerosmaiores(10,11,20,16)

def numerosmaiores1 (a,b,c,d): # aqui ele retorna o valor para numerosmaiores1 e para imprimilo eu tenho que botar dentro de uma abertura print
    if a>b and a>c and a>d:
        return a 
    elif b>c and b>d:
        return b
    elif c>d:
        return c 
    else:
        return d                     
print (numerosmaiores1(100,200,250,150))
#DICTIONARIES (uma forma de dados, que nem lista por exemplo q usa [] ou str, int etc.)
#nela vai se definir um valor chave que signifique aquilo, exemplos de meses de ano
#posso definir em um dictionary que jan representa janeiro, fev representa fevereiro, ou 1 representa janeiro, 12 dezembro e por assim vai
#ex: (em dictionary usa {} )
conversaomeses = {
    'Jan':'Janeiro',     #valores da esquerda do : são as chaves, não podem existir chaves iguais
    'Fev':'Fevereiro',
    'Mar':'Março',
    'Abr':'Abril',
    'Mai':'Maio',
    'Jun':'Junho',
    'Jul':'Julho',
    'Ago':'Agosto',
    'Set':'Setembro',
    'Out':'Outubro',
    'Nov':'Novembro',
    'Dez':'Dezembro',
}
#Há diversas maneiras de acessar os dados de um dictionary
#algumas maneiras abaixo:
print(conversaomeses['Jan']) #essa forma se consiste em chamar por um colchete a chave especifica, ou seja escrever exatamente a chave no dicionario
#mes = str(input('Digite as três primeiras letras de um mês: ')) //////// esse codigo funciona, so to deixando de comentário para não atrapalhar///
#print(conversaomeses[mes.capitalize()])                         /////////no resto do estudo, mas é outra forma de chamar por uma chave no dicionario//
print(conversaomeses.get('Mar')) #essa é outra forma
#usando o get dá uma possibilidade um pouco maior como no exemplo abaixo:
print(conversaomeses.get('luv','Não é um valor válido')) #nesse caso se escrever por exemplo valor invalido na lista como luv, vai aparecer uma
#mensagem de 'erro' escrito que não é um valor valido, isso pode ser usado para botar como padrão caso algum dado seja consultado de forma 'errada'
#OBS; posso armazenar qualquer valor que eu quiser em dictionary, então se eu quiser posso mudar a chave 'jan' para 1 por exemplo e assim por
#diante
boleano = True        #  significado de if boleano: é que: caso boleano seja verdadeiro:
if not boleano:         #  significado de if not boleano: é que caso boleano não seja verdadeiro:
    print('Verdadeiro') # os : pode substituir de certa forma os sinais de == praticamente
else:                   #
    print('Falso')      #
#FOR LOOP 
for ltra in 'Academia de giraffa':#Esse comando meio que diz que: para cada ltra na string 'academia de giraffa' exiba a letra, essa ltra é um valor
    print(ltra)                   #variavel e pode ser representado por qualquer outra coisa, por enquanto esse é o modo de ele exibir index por
#index, se por exemplo fosse uma lista eu poderia imprimir as listas por exemplo:
listateste = [[1,2,3],[4,5,6],[7,8,9]]
for cadalista in listateste:
    print(cadalista)#nesse exemplo ele imprime para cada lista na listateste ele vai imprimir a lista 1 2 e assim por diante por exemplo 
palavraaleatoria='comida de macaco'
for letra in palavraaleatoria:
    print(letra) # é o msm que o academia de giraffa, porém aqui é uma demonstração com uma variavel str
    print(palavraaleatoria)# nesse aqui acontece o seguinte, para cada letra vai imprimir a variavel palavraaleatoria, ou seja, se tiver 15 letras
#na variavel palavraaleatoria, vai imprimir palavraaleatoria 15 vezes, nesse caso não conta espaços em branco
for qualquerpalavravaiserviraqui in range(20):
    print (qualquerpalavravaiserviraqui-4) # aqui diz para cada 'indice'(q nesse caso ta com nome gigantesco de qualquerpalavravaiseviraqui porem
# nesses casos é bom usar i ou index quando for indicar 'alcance')
# no range (alcance) de 20, exiba o indice, ou seja é uma especie de contador nesse caso, q vai exibir 20 vezes em numeros crescentes começando 
#do 0, então ele nunca ira imprimir o ultimo número(nesse caso exibiria o 19), porém,  com ajuda de -4 ele pode começar d mais baixo ainda
#e terminar no 15 q nem está escrito no exemplo, porém há outra forma de fazer isso sem usar o -4 na frente q é na hora de definir o range
#q nem o exemplo abaixo:
for variavelqualquer in range(-10,20):
    print(variavelqualquer) #ele começa do -10 e vai até o 19, se quiser q ele va ate o 20 teria q botar 21 de alcance
#outra forma:
for index in range(len(palavraaleatoria)):#nesse caso como esta usando o len, ao invés de pegar 14 números tirando espaço como no exemplo 
    print(palavraaleatoria) #for letra in palavraaleatoria:print(palavraaleatoria), len conta os espaços em branco, fazendo assim contar 16
    #vezes ao invés de 14, nesse caso repetindo palavra 16 vezes
    print(palavraaleatoria[index])#nesse caso irá imprimir o indice das palavras, ou seja, o count deu 16 caracteres contando espaço, então 
    #vai pegar a palavraaleatoria e dar print(exibir né) as 16 primeiras letras dela por exemplo, se no caso do count daria 14 por exemplo ele
    #iria exibir letra por letra faltando as 2 ultimas, alco como c/o/m/i/d/a/ /d/e/ /m/a/c/a/
    print(palavraaleatoria[2])# nesse caso repetirá 16 vezes o index 2 de palavra aleatoria, q no caso seria o m de c o 'm' i d a ....
#OBS: A MAIORIA DOS FOR GERALMENTE É USADO COM LISTAS OU [] PORÉM VALE A PENA LEMBRAR NÉ
#outro exemplo interessante usando if no for:
for index in range(5):
    if index==0:
        print(index,'Primeiro')
    elif index==2:
        print(index,'tá no meio')
    elif index==4:
        print(index,'Último')
    else:
        print(index,'Não defini nada para aparecer aqui kk')
#forma de fazer uma potencialização (mais explicações em comentários adjacentes)
def potencializacao (numerobase,numeroexpoente): #praticamente fazemos o seguinte, especificamos que essa funcao vai ter numeroda base e o numero do expoente
    resultado=1 #aqui embaixo eu crio uma variavel para armazenar meus valores, inicialmente ela inicia com valor 1 para poder pegar qualquer valor (já que em potencializacao se elevar a 0 da 1, a gente usa 1 como valor minimo da equação nesse caso, como vai multiplicar dps, se pegarmos 0 para multiplicar ficaria dando 0 infinitamente)
    for index in range(numeroexpoente): #aqui dizemos que para o valor de número q a gente botou no expoente
        resultado = resultado * numerobase # vai fazer o resultado = 1 * numero da base, e dps q voltar dnv nele por conta do index de numeroexpoente, esse resultado vai guardar o valor de numerobase, agora multiplicando dnv por numerobase fznd potencialização
    return resultado

print(potencializacao(10,3))
""" 
q=int(input('Digite valor da base: '))                      # OUTRA FORMA DE FAZER O EXERCICIO DE CIMA, DE CERTA FORMA ACHO MAIS FACIL ESSE METODO
ex=int(input('Digite valor do expoente: '))                 # PORÉM SEMPRE BOM SABER DE OUTROS PARA CASOS ESPECIFICOS NÉ...
def pontecia(x,y):                   
    return q**ex
print (pontecia(q,ex))

"""
#LISTAS 2D e loop aninhado [loop aninhado é loop dentro de loop]
listateste = [
    [1,2,3],[4,5,6],[7,8,9],[0]
    ]
print (listateste[0][1])# nesse caso estou no primeiro index(0) chamando a linha e o segundo index(1) chamando a coluna
#assim como nos dois index acima o primeiro se referindo a linha e o outro a coluna, podemos moldar listas 2 d usando esses conceitos com loop
#for dentro de for como no exemplo abaixo:
for linhas in listateste: #esse primeiro valor se refere ao primeiro index, ou seja, para cada linha (começando de 0) na listateste:
    for colunas in linhas: # nesse segundo estamos dizendo, para cada coluna (que começa em 0 tmb) em linha, 
        print(colunas) #vai imprimir cada coluna (comecando do 0) até a quantidade de index tiver em linhas
#O que o codigo acima faz praticamente é o seguinte, usando de exemplo listateste q possui valores de 0 até 9 (vou fazer uma releitura do cod:)
#para cada quantidade de linhas que tiver em lista teste ( oou seja, existem 4 linhas, a linha index 0 que é do 1-3, a index 1 q é da 4-6, a index 2 que é de 7-9 e a index 3 que é o 0)
#para a quantidade de linhas em listateste(que é 4, ou seja, vai repetir esse loop 4 vezes)
# e para cada colunas q tiver em linha(q nesse caso é 3)
#ou seja, o codigo vai repetir o primeiro for 4 vezes, porém em cada um dessas repetições, ele vai repetir 3,3,3,1 vezes respectivamente por conta das colunas
#nesse caso ele daria 'print' por assim dizer exatamente 10 vezes se eu tiver certo, verifique, na primeira repeticao ele vai printar 3 numeros,
#na segunda mais 3, na terceira mais 3 e na ultima mais 1

#fazendo um 'tradutor'
#vamos fazer um tradutor que pegue uma palavra e transforme todas vogais em g por exemplo
#vamos começar definindo a 'função' desse tradutor
def tradutor (frase): #defina tradutor que tem o parametro frase, ou seja, frase é a variavel q vamos chamar dentro dessa def 
    traducao =''#aqui é como vai ficar nossa frase dps de traduzir, vamos deixar ela em branco para podermos definir como variavel dps
    for letra in frase: #para cada letra na frase faça:
        if letra in 'AEIOUaeiou':# se tiver AEIOUaeiou na letra faça: ##outra forma aqui seria botar letra.lower() in 'aeiou' [facilitando assim escrever apenas as letras minusculas né...]
            traducao = traducao + 'g' #traducao = traducao + g (q irá trocar o valor das vogais por g né)
        else:#senao
            traducao = traducao + letra#se nao tiver nenhuma das letras acima apenas repita a letra 
    return traducao # aqui com o valor formado, retorne a frase que se transformou:
#print(tradutor(input('Digite uma palavra para \'decodificar\': ')))

### No exemplo acima tem um problema, se botarmos uma vogal maiuscula ele vai trocar por um g minusculo, podemos corrigir isso botando outra declaracao if:
def tradutor (frase): 
    traducao =''
    for letra in frase: 
        if letra.lower() in 'aeiou':
            if letra.isupper():
                traducao = traducao + 'G' 
            else:
                traducao = traducao + 'g' 
        else:
            traducao = traducao + letra
    return traducao
print(tradutor('Ola, apenas um teste'))
##
#### TRY / EXCEPT : isso evita o codigo parar de ocorrer por conta de um erro, por exemplo:
#testandotry = int(input('Digite um número: '))/// #Se colocarmos uma letra ou float nesse input, o código dará erro e ira parar de executar caso seja 
#print (testandotry)////////////////////////////// #inserido um valor invalido , para isso podemos usar Try e Except 
#--------------------####----------Deixei em modo comentário para não rodar no codigo mas tá ai de exemplo encima e embaixo a utilização básica
#de try e except que resumidamente é: tente fazer x coisa, caso não de certo(ou caso ocorra um erro né) faça: ....------------------###----------
try:
    testandotry=int('String completamente errada apenas para teste de erro, afinal tá declarando que é int e eu to botando uma str')
    print(testandotry)
except:
    print('Valor inválido.') 
#__________________________Dessa maneira, tudo que for colocado dentro do try ira se aplicar para o except, o que torna o except geral para todos,
#porém para evitar isso podemos especificar mais outras coisas no except como no exemplo abaixo:
try:
    testandotry=int('String completamente errada apenas para teste de erro, afinal tá declarando que é int e eu to botando uma str')
    print(testandotry)
    valor = 10/0          #conta que daria erro, porém é causa da divisão por 0 e nao por input errado, então dará valor inválido para essa 
except: # equacao tmb, podemos entao definir para cada except como no outro exemplo abaixo desse:
    print('Valor inválido.') 
#====================================================================================#=========================================================#
try:
    testandotry=int('String completamente errada apenas para teste de erro, afinal tá declarando que é int e eu to botando uma str')
    print(testandotry) #nesse modelo, ira printar equivalente a cada um do erro dependendo de qual ocorrer de errado, se o primeiro ocorrer errado
    valor = 10/0#ele já encerra antes de ir p segundo então não irá ser printado dois ao msm tempo, porém enquanto não estiver correto ele não
except ZeroDivisionError as err:#avançará para frente
    print(err)#usando AS ERR declaramos que armazenaremos o erro como err e podemos por exemplo printá-lo, nesse caso exibiria o erro 'division by zero'
except ValueError as alo:#que foi o erro que aconteceu
    print(alo,'abc')
except FileNotFoundError:
    print("Arquivo não encontrado")
# READING FILES#
#tem outro arquivo .txt com nomes de empregados, para abrir usa:
open("sequenciaestudopython - empregados.txt",'r')#esse comando significa que: abra o arquivo x, 'r' é abreviacao para read, ou seja, vai apenas ler
#não vamos poder modificar (também existe o w que é de write que permite modificar o arquivo, existe 'a' que é append, que vai acrescentar ao final
# do arquivo, não podendo modificar. existe tmb 'r+' que é ler e escrever.)[também tem 'a' que é append que é para extender, por exemplo em caso de
# uma lista que tem 5 pessoas e vc quer acrescentar mais uma, vc usa o 'a' (adicionará no final do texto)]
#porém não é só isso, precisamos definir para esse arquivo uma variavel tmb
empregadoss = open("sequenciaestudopython - empregados.txt",'r')
#print(empregados.readable())#com esse comando poderemos verificar se o arquivo está legivel, ele ira retornar valor boleano (True ou False)
#print(empregados.read())#esse comando irá cuspir todas informações do arquivo quando executarmos o programa
"""
print(empregados.readline())# esse comando irá apenas ler 1 linha, começando sempre da 1°, ou seja, se dermos esse comando denovo, ele vai ler a linha
print(empregados.readline())#posterior também 
print(empregados.readline())
print(empregados.readline())
print(empregados.readline()) # nesse caso como so temos 5 linhas com conteúdo, a partir da próxima linha, vai ler a próxima linha, porém como não
print(empregados.readline())# existe uma próxima linha, ele irá imprimir espaço em branco
print(empregados.readline())
print(empregados.readline())
print(empregados.readline())
print(empregados.readline())
print(empregados.readline())
print(empregados.readline())
print(empregados.readline())
"""
##-----Porém existe outro comando para imprimir diversas linhas em mais de uma vez doq repetindo readline:
#//////print(empregados.readlines()[0])//////# esse comando transformará o arquivo em uma lista [] (assim cada item tera um valor index atribuido)
# podemos também chamar as linhas de arquivos com comando for:
for empregados in empregadoss.readlines():#com esse for loop podemos imprimir na tela todos empregados(linhas) existentes em empregados.readlines()
    print(empregados)
empregadoss.close() # aqui fecha o arquivo, então o python não vai mais conseguir ler além disso no arquivo, não conseguirá acessa-lo denovo além desta linha

"""
lista2=[]
while count < 2:
    lista2=lista2+[int(input('Digite um nome:'))]
    count += 1
print(lista2)
"""
empregadoss = open("sequenciaestudopython - empregados.txt",'a')
print(empregadoss.write('\nTyler - Diretor')) #muito cuidado ao usar o write em geral (inclusive a variacao dele que é o 'a' para acrescentar no 
#final) porque é facil virar uma bagunça(de no caso você rodar o programa duas vezes com write por exemplo ele escreverá o mesmo comando duas 
# vezes), se não declarar \n para pular linha, os textos serão inseridos tudo em fila.
##OBS; nota que no teste que eu usei, usei um arquivo .txt, então se eu deixar uma linha em branco no meu arquivo txt ele começa ja na linha de baixo
#uma obs interessante que pode acontecer algum erro eventualmente.
empregadoss.close()

#writefile
empregadoss = open("printpythontestecomandowrite.py",'w')#nesse arquivo eu usei uma copia de empregados.txt, com o 'w', ele vai sobrescrever
#o arquivo inteiro. eu tambem posso criar qualquer nome de arquivo e qualquer arquivo desde que eu bote .extensao na frente como nos exemplos escrito
#uma vez criado nessa mesma pasta, um novo comando write ira sobreescrevelos inteiramente, ou seja, ele não adicionara algo no que ja existe
#e sim substituir o que tem pelo q vc escreveu, até o momento de estudo a unica coisa q daria p vc fazer caso quisesse adicionar um novo item
#seria usar o comando 'a'
empregadoss.write("print('Ratomanocu')\n")
empregadoss = open("printpythontestecomandowrite.py",'a')
empregadoss.write("print('brincadeira')\n")#aqui ele não ira adicionar infinitamente conforme vce rodar o programa, porque em ordem o que executa
#primeiro é o write q vai criar uma nova lista sobreescrevendo oq ja tinha, e dps vai chegar no 'a' que vai adicionar o print brincadeiraa, então quando
#você executar o programa, ele vai começar a ler denovo: o arquivo q tinha 2 linhas vai ser sobrescrito por ratomanocu, e dps vai ser adicionado 
#brincadeiraa
print(empregadoss)
empregadoss.close()

# python module and pip 
#criei outro arquivo de python com algumas funcoes e variaveis dentre elas rodar um dado por exemplo, o primeiro passo vai ser importar esses dados
#usando import e o nome do arquivo ( que infelizmente eu botei um nome muito grande =( )
import arquivocomplementarmodulo #python é 'inteligente' suficiente para reconhecer o arquivo, python, mas ficar de olho nisso em eventos futuros
#para usar os arquivos eu tenho que botar o nome do import, entao:
print(arquivocomplementarmodulo.metros_para_km)#depois do nome do modulo que você importou, você precisa botar o . para puxar qualquer codigo do
#arquivo modulo
ooooo=int(10)#tmb funciona com input, soq eu botei como texto p evitar ter q ficar marcando cxnha toda hora q executar =)
print(f"Resultado é {arquivocomplementarmodulo.metros_para_km*ooooo}")
print(arquivocomplementarmodulo.rodardados(6))
#python object and classes
""" #VOU DEIXAR EM MODO COMENTÀRIO MAS VAI ESTAR ESSE CODIGO E A SEQUENCIA EM OUTRO ARQUIVO PARA MIM PODER \n"IMPORTAR\n"
class estudantes:#comece com class e depois o nome que você vai dar para essa classe seguida com :
    def __init__(self,nome,ano,notamedia,matriculado ):#estou declarando que o __init__ que é initialize (inicializar) estou declarando que 
#começando a declarar no caso né que a class estudantes possui nome(str), ano(int), notamedia(float), matriculado(bolean), estou declarando que
#estudantes possui essas 4 formas de dados##esse valor self pode ser alterado por qualquer q voce quiser, ele é uma variavel para atribuir outros valores
        self.nome = nome
        self.ano = ano
        self.notamedia = notamedia
        self.matriculado = matriculado
"""
#import estudantesclasse # não tenho certeza se essa pode ser uma opção, mas se isso for mt grande podemos acabar pegando arquivos desnecessarios
#e deixar o arquivo mais pesado atoa, podemos so pegar oq nos queremos:
from estudantesclasse import estudantes #aqui esta dizendo q: do arquivo estudantesclasses.py, import (traga p cá) estudantes (que é o nome da classe
#no arquivo)
estudante1 = estudantes('Alexandre','Informática',2.5,True)#uma classe é o esboço que define o que é um estudante nesse caso, e um objeto (produto
#criado por uma classe) já é um objeto que contém valores
estudante2 = estudantes('Alexandre','Logica programação',10,True)
print (estudante1.nome)#aqui podemos definir qual informação sobre estudantes queremos pegar usando . , ou seja, tmb podemos fazer:
print(estudante1.nomecurso)
if estudante1.notamedia >= 6:
    print('Aluno com notas acima da média')
else:
    print('Aluno com notas abaixo da média')
if estudante1.matriculado == True:
    print("Aluno com matricula ativa")
else:
    print('Aluno com matricula inativa ou cancelada')
print (estudante2.nome)#aqui podemos definir qual informação sobre estudantes queremos pegar usando . , ou seja, tmb podemos fazer:
print(estudante2.nomecurso)
if estudante2.notamedia >= 6:
    print('Aluno com notas acima da média')
else:
    print('Aluno com notas abaixo da média')
if estudante2.matriculado == True:
    print("Aluno com matricula ativa")
else:
    print('Aluno com matricula inativa ou cancelada')
from estudantesclasse import motorista
from random import *
isrnome=str('alexandre')
motorista1 = motorista(isrnome,'AB')
if isrnome == isrnome.capitalize():
    None
else:
    motorista1.nome = isrnome.capitalize()
    isrnome = isrnome.capitalize()
print(motorista1.nome)
print (isrnome)
"""
from estudantesclasse import fruta
fruta1 = fruta('banana','amarelo')
fruta2 = fruta('maçã','vermelho')
fruta3 = fruta('ameixa','roxo')
print('Qual a cor da banana?\n1-Amarelo\n2-Vermelho\n3-Roxo')
print('Qual a cor da maçã?\n1-Amarelo\n2-Vermelho\n3-Roxo')
print('Qual a cor da ameixa?\n1-Amarelo\n2-Vermelho\n3-Roxo')
print('Digite o nome em sequência nas respostas:')
nada = []
for i in range(0,3):
    noda = [str(input())]
    nada += noda
if fruta1.cor == nada[0] and fruta2.cor == nada[1] and fruta3.cor == nada[2]:
    print('Acertou todas')
elif fruta1.cor != nada[0] and fruta2.cor == nada[1] and fruta3.cor == nada[2] or fruta1.cor == nada[0] and fruta2.cor != nada[1] and fruta3.cor == nada[2] or fruta1.cor == nada[0] and fruta2.cor == nada[1] and fruta3.cor != nada[2]:
    print('Acertou duas')
elif fruta1.cor != nada[0] and fruta2.cor != nada[1] and fruta3.cor == nada[2] or fruta1.cor != nada[0] and fruta2.cor == nada[1] and fruta3.cor != nada[2] or fruta1.cor == nada[0] and fruta2.cor != nada[1] and fruta3.cor != nada[2]:
    print('Acertou uma')
else:
    print('Errou todas')
"""
#Fazendo jogo de multiplas escolhas, algumas explicacoes: existem 3 exemplos, apenas ler dessa para baixo
print("IMPORTANTE, CONTEUDO ABAIXO, TIVE QUE DEIXAR EM MODO COMENTARIO PARA QUE OS INPUT NÃO ATRAPALHE NA HORA DE EU TESTAR OS DEMAIS CÓDIGOS")
print("IMPORTANTE, CONTEUDO ABAIXO, TIVE QUE DEIXAR EM MODO COMENTARIO PARA QUE OS INPUT NÃO ATRAPALHE NA HORA DE EU TESTAR OS DEMAIS CÓDIGOS")
print("IMPORTANTE, CONTEUDO ABAIXO, TIVE QUE DEIXAR EM MODO COMENTARIO PARA QUE OS INPUT NÃO ATRAPALHE NA HORA DE EU TESTAR OS DEMAIS CÓDIGOS")
print("IMPORTANTE, CONTEUDO ABAIXO, TIVE QUE DEIXAR EM MODO COMENTARIO PARA QUE OS INPUT NÃO ATRAPALHE NA HORA DE EU TESTAR OS DEMAIS CÓDIGOS")
"""
from estudantesclasse import perguntas
questoes = [ #aqui defino uma lista contendo todas as perguntas com as opções, vou usar ela depois, é importante que ja formule aqui como se ja fosse
"Qual a cor da banana?\n(a)Amarela\n(b)Vermelha\n(c)Roxa\n",#o terminal, por exemplo, já elabore de uma forma que a resposta vai ser encaixada aqui
"Qual a cor da maçã?\n(a)Amarelo\n(b)Vermelho\n(c)Roxo\n",#embaixo, tipo, qual o resultado da expressao \n 1 \n 2 \n 3 \n (espaco em branco p resposta)
"Qual a cor da ameixa?\n(a)Amarelo\n(b)Vermelho\n(c)Roxo\n"
]
listaresposta = [ #aqui vamo definir o seguinte, tem outro arquivo que está criando objetos com a classe perguntas, que define duas coisas, qual a pergunta
    perguntas(questoes[0],'a'),# e qual a resposta, exemplo, a funcao perguntas vai receber dois atributos, a pergunta, e a resposta equivalente a ela
    perguntas(questoes[1],'b'),#nesse caso, questoes[0] é o item da lista acima que representa a pergunta e tem as opcoes de resposta p gente escolher
    perguntas(questoes[2],'c'),#entre a,b e c, como ta na lista acima, e logo depois, uma virgula, e uma string com a resposta certa (entre a,b e c)
]                                                                            
def respostas(a): #aqui tamo definindo uma funcao chamada respostas, você pode botar o nome que quiser, porém seria util você botar de alguma
#maneira que você consiga reconhecer depois mais facil, e dentro dos parenteses o atributo que precisa estar dentro para executar, mais uma vez,
#você deve colocar algo que seja mais facil de visualizar e abstrair e entender, pois como eu disse, voce pode botar o nome que quiser,
# ele não ira interferir com o resto do arquivo
    b = 0 #nos outros dois exemplos mais abaixo, está melhor definido o nome dessas variaveis, mas resumidamente essa equivale a pontuacao da pessoa,
#ou seja, é um jogo de acertar e isso aqui é a variavel q vai indicar no final quantas respostas o usuario acertou corretamente
    for c in a:#sempre lembrando de botar um nome melhor aqui, mas vamos lá, vamos seguir o exemplo que está aqui, você vai botar na hora de puxar
#essa funcao, um atributo representado por 'a', entao aqui está praticamente dizendo: para cada item de a, faça:
        d = input(c.comando)#d é outra variavel q voce deve colocar um nome e nesse contexto é a resposta, entao: resposta = input(c.comando), esse
#c.comando vai puxar do item, ou seja, nesse caso .comando se refere a um objeto especifico, então é de suma importancia nesse caso que todos item
# do atributo q você vai enviar para funcao respostas, sejam objetos para puxar classes, entao diz que, vai puxar a sigla do objeto na sua classe 
#que vai ser c, que é o mesmo nome q você botou em 'for c in a', pq se você ler, para cada item na listaresposta, começa com o objeto perguntas,e
#comando é o nome do primeiro atributo dele que representa nesse exemplo questoes[0],questoes[1] e questoes[2],entao o comando basicamente está dizendo
#que a variavel d (que é resposta), ou seja, a resposta é input do usuario e oq vai aparecer para o usuario dar input é o texto escrito no c.comando
        if d == c.resposta:# e aqui vai fazer a comparacao, no listaresposta está posto a pergunta e em seguida a resposta, sao os 2 atributos do 
#objeto, entao aqui é uma pergunta simples: se resposta for igual a resposta que na lista executando atual (como sao 3 items e tem um for in ele
# vai executar o comando a quantidade de linha q tiver), vai fazer o seguinte:
            b += 1#a pontuacao vai aumentar em 1
    print('Das suas respostas,',b,'/',str(len(a)),' foram corretas .')#aqui vai apenas imprimir na tela, b a pontuacao e para contar quantos itens
# tem na lista, usa len(nomedoitemqvcvaiprecisarparachamarfuncao) e como ele volta um valor inteiro, para nao ter problemas precisamos converter
#esse valor para uma string que é texto, então basta antes usar str(len(a)).
respostas (listaresposta) # e aqui é onde começa tudo, você tem que fazer uma funcao (def) já em mente para o que vai servir, nesse def de respostas
#se refere a uma lista de perguntas e respostas, então primeiramente a gente cria um objeto para comportar 2 valores que serão respectivamente
# a pergunta e a resposta e a unica maneira de fazer isso é usando uma classe, então depois o que a gente precisa para executar essa funcao, é chamar
#ela no caso botei o nome de respostas, e o atributo dentro do parenteses dentro dela tem que ser o requisito para que a gente definiu a funcao
#que é uma lista de objetos 
"""
"""
from estudantesclasse import perguntas
questoes = [
"Qual a cor da banana?\n(a)Amarela\n(b)Vermelha\n(c)Roxa\n",
"Qual a cor da maçã?\n(a)Amarelo\n(b)Vermelho\n(c)Roxo\n",
"Qual a cor da ameixa?\n(a)Amarelo\n(b)Vermelho\n(c)Roxo\n"
]
listaresposta = [
    perguntas(questoes[0],'a'),
    perguntas(questoes[1],'b'),
    perguntas(questoes[2],'c'),
]                                                                            
def respostas(listaresposta):
    pontuacao = 0
    for perguntas in listaresposta:
        respostass = input(perguntas.comando)
        if respostass == perguntas.resposta:
            pontuacao += 1
    print('Você acertou',pontuacao,'/',str(len(listaresposta)),'.')
respostas (listaresposta)"""
"""
from estudantesclasse import question
question_prompt = [
"Qual a cor da banana?\n(a)Amarela\n(b)Vermelha\n(c)Roxa\n",
"Qual a cor da maçã?\n(a)Amarelo\n(b)Vermelho\n(c)Roxo\n",
"Qual a cor da ameixa?\n(a)Amarelo\n(b)Vermelho\n(c)Roxo\n"
]

questions = [
    question(question_prompt[0],'a'),
    question(question_prompt[1],'b'),
    question(question_prompt[2],'c'),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got",str(score),'/'+str(len(questions)),'correct')

run_test(questions)"""
#OBJECTS FUNCTIONS
#pode alterar funcoes de objetos, conteúdo e ate msm fornecer alguma informacao especifca
from estudantesclasse import estudantes1
estudante10 = estudantes1('Alexandre','Desenvolvimento de Software Multiplataforma',8.3)
estudante11 = estudantes1('Alexandre','Informática',5.9)
print(estudante11.elite()) #esse é um exemplo de funcao em objetos, o codigo tá no arquivo estudantesclasse.py
#INHERITANCE     PARA PORTUGUES: HERANÇA
#inheritance é sobre a gente pode criar um monte de funcao para um objeto de uma classe, e depois podemos fazer outros objetos de outras classes
#herdar essas funcoes, vou criar nova classe e objeto para demonstracao
from estudantesclasse import chefe
meuchefe = chefe()
meuchefe.fazeralmoco()
#quando rodar o programa vai imprimir 'preparar almoço'
from estudantesclasse import chefechines
meuchefechines= chefechines()
meuchefechines.fazerjanta()
