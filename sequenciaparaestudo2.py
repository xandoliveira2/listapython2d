#sequencia p estudo 2
minhalista = ['maçã','banana','cereja','r4gn4r0s'] # podemos criar elementos dentro de uma lista se separarmos por virgula
print(minhalista)
minhalista2=list() #podemos declarar que uma variavel é uma lista
minhalista3=[5,2.45,True,'Olá mundo','Olá mundo'] # uma lista pode conter numeros inteiros, decimais, caracteres e booleanos, imagino eu q até mesmo tupla 
#seria uma opção, podemos até mesmo repetir um elemento
minhalista4 = [{1,3},{2,4}]
print(minhalista2)
print(minhalista3)
print(minhalista4)
item  = minhalista4[1] #tmb podemos definir algo em especifico dessa lista usando index(lenbrando que começa do 0, então o 1° item se refere ao
#index 0)
print(minhalista[-3]) #podemos indicar index negativo para uma lista tmb, porém ela tem o limite dela, no maximo de item, então se existem 10 item
#na lista, o maximo que podemos botar é -10, e tecnicamente ela vai puxar o inverso, supondo na lista minhalista tem maça banana e cereja, index
#0 é maça, 1 é banana e 2 é cereja, o index negativo percorre inverso, -1 é cereja, -2 é banana e -3 é maça
print(item)
#para exibirmos os itens da lista podemos usar um for
for i in minhalista:
    print(i)
#para checar se tem um item dentro da lista você pode usar if:
if 'banana' in minhalista:#ele vai buscar exatamente a palavra banana, se tiver faltando uma letra não reconhecera
    print('tem')
else:
    print('não tem')

for i in minhalista:
    if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i: # tmb podemos fazer comparações assim, perguntar se tem uma letra em especifica
        print(i,'Tem vogal') #de exemplo eu dei de vogal ##deve haver alguma maneira mais simples, mas essa é a q tem por agr
    else:
        print(i,'Não tem vogal')
#também podemos contar quantos items tem em nossa lista usando funcao len
print(len(minhalista))
if len(minhalista) == 1:
    print('1 itens')
elif len(minhalista) == 2:
    print('2 itens')
elif len(minhalista) == 3:
    print(' itens')
elif len(minhalista) == 4:
    print('4 itens')
else:
    print('5 itens ou mais')
#podemos adicionar itens tmb a lista usando append (também funciona com input se você colocar corretamente)
#obs> para adicionar em input seria algo mais ou menos assim:
#minhalista = list()
###a cada input q você for dar tem q declarar q o valor dela se acumulará, entao ficaria para cada input algo como:
#nome = input()
#minhalista = minhalista + nome 
minhalista.append('limão')
#metodo acima adicionou no final da lista um item chamado limao, entao quando eu der print vai ter limao:
print(minhalista)
#também tem metodo .insert que a gente pode inserir um item em determinado lugar da lista:
minhalista.insert(1,'Uva') # vai adicionar no index 1 de minha lista, então oq ta em 1 vai ir p index 2 e oq tá no index 2 p 3 e ai por diante ate
#o final da lista
print(minhalista)
itemremovido = minhalista.pop() # esse metodo exclui o ultimo item da lista, porém tem como remover outro, porém tem como fazer outro que exclui um determinado index
itemremovido2 = minhalista.pop(2)# basta colocar o numero do index q você quer remover como no exemplo a esquerda dessa frase
itemremovido3=minhalista.remove('Uva')# outra forma de remover um determinado item é botando exatamente o qual você quer remover
                                    # porém com metodo remove como no exemplo a esquerda ##obs: caso não tenha o elemento que você botar no remove
                                    # vai dar erro
print (minhalista)
print(itemremovido) # podemos também pegar esses valores q foi removido caso quisermos fazer algo especifico
print(itemremovido2)
print(itemremovido3) # aqui vemos claramente que o item não pode ser armazenado, uma vez escrito remove ele é excluido, e pop ele é retirado da lista
try:
    itemremovido4=minhalista.remove('Uva12')#botando em try pode evitar dar erro q pare o programa
except:
    print('hola')
print('olá')
#podemos também limpar a lista usando metodo clear:
print(minhalista2.clear())
minhalista2.append('Uva')
print (minhalista2)
#podemos também reverter a ordem da lista com metodo reverse:
minhalista = ['maçã','banana','cereja'] # dando um reset na lista 
minhalista2 = [1,4,6,10,2,7]
minhalista2.reverse() #esse metodo inverte a lista, porém diferente de outros que cria uma copia, esse altera o original, então você precisa
#declarar q está invertendo ele p depois poder printar
minhalista.reverse()
print(minhalista)
print(minhalista2)
minhalista.sort()# a mesma coisa que acontece em reverse acontece em sort, ele altera o original e não faz uma copia, então você primeiro declara
minhalista2.sort()# que sua lista está sendo ordenada (sort) em ordem (crescente ou alfabetica) ##obs> esse comando não funcionará em lista que 
print(minhalista2)#possui str e int.
print(minhalista)
minhalista = ['maçã','banana','cereja',1,100]
minhalistaiterator = reversed(minhalista)#... ok ...isso vai ser bem dificil de explicar kkkk praticamente é o seguinte, se você não quiser q seja 
minhalistal = list(minhalistaiterator)#alterado do original, você vai usar o metodo reversed q vai criar uma cópia invertendo, porém ele vai ser
print(minhalistaiterator)# criado com codigo, para poder exibir esse item precisamos criar outra variavel que recebe a copia 'revertida' do metodo
print(minhalistal)# e transforma em uma lista, então declaramos na nova variavel que vai o objeto criado pelo metodo reversed vai ser uma lista
                    # de forma resumida um iterador vira um objeto ou imagina q vira um container
                    #sinceramente isso dá muito trabalho, se não quiser que altere sua lista é mais facil você criar uma lista secundária e 
                #atribuir o valor igual e depois usar a funcao como por exemplo:
minhalista10=minhalista
minhalista10.reverse() # muito mais facil assim
print(minhalista10)
minhalista = ['maçã','banana','cereja']
print(sorted(minhalista)) #esse aqui diferente do reversed ele não cria um iterable, ele cria uma copia organizada de fato
print(minhalista) 
#podemos também usar multiplicadores (*) dentro de listas, por exemplo:
listaexemplo = [0] * 5
print (listaexemplo) # ele ira imprimir o numero 0, cinco(5) vezes, o mesmo podemos fazer alterando os valores como por exemplo:
listaexemplo = [[0]*5,[10]*2]
print(listaexemplo)
listaexemplo = [(10*20)+(20)+100*2] # também podemos somar números em listas se for colocado como parenteses com as mesmas regras matematicas,
print(listaexemplo)# primeiro parenteses,depois potencia e raiz quadrada,depois multiplicacao e divisao, e dps adicao e subtracao.
#também podemos juntar listas, como por exemplo:
listaexemplo=[[0]*5,[10]*2]
listaexemplo2 = [1,2,3,4,5,6,7,8,9,10]
listaexemplo3= listaexemplo + listaexemplo2
print(listaexemplo3)
#podemos também separar conteudo de uma lista usando index inicial : index final:
a = listaexemplo3[0:4] # aqui atribui o valor de a o index de 0,4 que vai ser os 4 primeiros valores, então:
b = listaexemplo3[:4] # se não botar nada no valor inicial vai printar do primeiro até onde você definir o final, o mesmo acontece ao contrario
c = listaexemplo3[3:]
print(a) # é interessante ressaltar que, o primeiro termo de listaexemplos3 é um conjunto de 5 zeros, então ele vai imprimir esse conjunto que representa
print(b)
print(c)
print(listaexemplo3)# o index 0, dps o index 1 q representa 2 numeros 10, e dps o index 2 e 3 que representam respectivamente 1 e 2, e mmais um detalhe
#a se obeservar é que mesmo separando conteudo index de 0:4 na variavel a, ele não deixa de existir na lista primária
#Podemos também declarar em quantos 'passos'(step) vai mostrar na lista, entao por exemplo:
print(listaexemplo3[::1]) #padrao, vai pular 1 item por vez, entao vai mostrar todos
print(listaexemplo3[::2])# vai pular 2, entao vai mostrar o index 0,2,4,6,8,10... e por ai vai
print(listaexemplo3[::3])#aqui mesma coisa, mas vai pular 3...
#se botar número negativo vai reverter a ordem e também vai ter o mesmo quesito de 'passos' (steps)
print(listaexemplo3[::-1])#vai começar do ultimo index pegando e pulando 1 passo, entao ex em uma lista 1,2,3,4,5,6,7,8,9,10 vira 10,9,8,7,6,5,4,3,2,1
print(listaexemplo3[::-2])#vai começar do ultimo index e pulando 2 passo, ex: a lista é 1,2,3,4,5,6,7,8,9,10 vira 10,8,6,4,2
print(listaexemplo3[::-3])#vai começar do ultimo index e pulando 3 passo, ex: a lista é 1,2,3,4,5,6,7,8,9,10 vira 10,7,4,1 
#para copiar um arquivo pode dar alguns problemas algumas vezes, como no exemplo abaixo:
lista = ['maça','laranja']
lista2 = lista
print(lista)
print(lista2) # dando print, ambos tem o mesmo valor agora, porém , se eu usar .append na lista2 que é uma copia olha oq vai dar
lista2.append('limão')
print (lista) # ambos são influenciados, pois diz q lista2 = lista, então se lista2 mudar, lista 1 tmb muda, para ter certeza que você tá criando
print(lista2)#uma copia, use o metodo copy como abaixo
print('~~depois de usar .copy()~~')
lista = ['maça','laranja']
lista2 = lista.copy()
lista2.append('limão')
print(lista)
print(lista2)
#outra forma de você fazer uma copia seria declarando:
lista = ['maça','laranja']
lista2 = list(lista)
lista2.append('limão')
print(lista)
print(lista2)
#algo bem interessante fazer em lista é criar uma definicao de numeros, por exemplo vamos supor q tenhamos a lista 1,2,3,4,5
lista = [1,2,3,4,5]
#e agora queremos que para os itens da lista apareca a potencia ao quadrado, então agora declaramos:
potencia = [i*i for i in lista]#aqui praticamente diz que, para cada item na lista, vai multiplicar ele por ele mesmo, então seguindo a logica pode-
#riamos até mesmo criar ao cubo, como:
cubo = [i*i*i for i in lista]
print(lista)
print(potencia)
print(cubo)
texto = 'texto teste para exibicao em fstring'
#usando o metodo .title() que vai dar um capitalize em cada letra, ou seja, cada primeira letra vai ficar maiuscula (também pode ser usado dentro
# de uma f'string')
print(texto.title())
cpf = 421234512 # nesse exemplo significa, cpf = 421234512, porém nos sabemos que cpf tem 11 digitos, então esse é um erro de formatacao, pois 
#o python ou qualquer coisa matematica, não reconhece zeros a esquerda, então, para fazer de um jeito funcional, tem 2 possibilidades, você colocar
#como uma string, ou formatar na hora do f'string' como vai ser no no exemplo abaixo
print(f'cpf: {cpf:011}')# representa oq, na variavel cpf, vai ter 0 a esquerda e o limite de numeros q pode ter são 11, interessante que o unico
#valor que pode atribuir o 0 no começo é para preencher com 0's a esquerda se não cumprir o limite, ja q se eu trocar por 111 por exemplo ele se
# tornaria       (102 espaços em branco )                 421234512 (o resto dos 9 digitos para dar 111)   
faturamento = 1000
print (f'{faturamento:.2f}')
print(f'faturamento: {faturamento:,.2f}') #usando virgula podemos definir a virgula como casa de milhar (1000+)
print(type(faturamento))
print (type(cpf))
print (type(texto))
from datetime import datetime    #importar funcoes de tempo
hoje = datetime.now() #declarando variavel hoje com a funcao datetime.now() q em traducao livre é datatempo agora
print(f'data: {hoje:%d/%m/%Y}, horario: {hoje:%H:%M}') #Para datas também temos uma facilidade bem maior, só que aqui temos alguns comandos um pouco
#diferentes, pois precisamos inserir o % + a inicial do que vamos mostrar.
#Então temos “d” para dia, “m” para mês e “Y” para ano. Isso porque as siglas são em inglês, então temos que utilizar esse padrão. O mesmo vale para 
# horas e minutos.
#posso encontrar mais detalhes em: (sobre pq foi usado d m Y etc...)
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

#_____SOBRE TUPLE_____
#tuplas são valores imutaveis, de certa forma eles seguem o conceito de lista em boa parte dele, tirando o fato q não podem ser alterados enquanto
#seu tipo for uma tupla, então por exemplo:
minhatupla = tuple([1,2,3,4,6,7]) #para criarmos uma tupla usando a classe 'tuple' precisamos botar os elementos dentro dessa tupla em formato de lista
minhatupla2 = (5,4,3)# caso não queira usar class tuple, pode botar direto entre parenteses que o python já vai reconhecer como tal
print(minhatupla)
print(minhatupla2)
# e para puxar elementos é a mesma coisa em lista em index, count e len(dentre outros), então:
print(len(minhatupla))# vai contar o números de elementos da tupla
print(len(minhatupla2))
print(minhatupla2.count(3)) # vai contar quantas vezes o 3 aparece no minhatupla2 (que vai ser 1)
print(minhatupla.count(9)) # vai contar quantas vezes o 9 aparece na minhatupla (que vai ser 0)
print(minhatupla2[2]) # vai printar o index 2 de minha tupla (que é 3)
print(minhatupla[5])# vai printar o index 5 de minha tupla (que é o 7)
print(minhatupla2.index(4))#vai printar o index que o elemento '4' está, nesse caso ele é o segundo elemento de minhatupla2 que é index 1
print(minhatupla.index(6))#vai printar o index que o elemento '6' está, nesse caso ele é o quinto elemento de minha tupla que é index 4
#podemos transformar uma tupla em lista e vice versa declarando, então por exemplo:
minhalista2 = [1,2,3,4,5,6,7,8,9]
minhalista1 = list(minhatupla)
print (minhalista1)

minhatupla3 = tuple(minhalista2)
print(minhatupla3)

#também podemos pegar elementos de uma tupla:
a = minhatupla[1:4:2] #as mesmas regras d lista, 1:4 é do index 1 até o 4 porém não inclui o 4, msm se botar 2: fica do segundo index ate o final
# e :3 é do primeiro index (o index 0) até o index 3 (que não é incluso, então vai pegar index 0 1 e 2)
#e a msm coisa para definir steps (passos que vai dar) usando ::2 por exemplo q vai pular de 2 em 2
#fomatos de steps:
#voce pode definir com um valor de começo e fim dps de passo como: 1:5:2 (do index 1 ao 5 [que nao vai ser incluso] pulando 2 casas entre eles)
#ou você pode definir como ex: 1::2 (do index 1 até o final pulando 2 casas)
# a mesma coisa se vc n definir o começo, exemplo> :5:2 ( vai do primeiro index até o 5 pulando 2)
# e usando números negativos no passos a gente inverte a ordem da lista, podemos usar -1 q vai reverter toda lista/tupla, -2 inverteria a tupla
# mostraria de 2 em 2 'passos' (step)
print(a)
tuplaunpacking = ('Alexandre',20,'São Paulo')
#podemos 'desempacotar' (unpacking) tuplas, então posso definir que:
nome,idade,estado = tuplaunpacking #como sei que tuplaunpacking tem 3 valores, estou declarando respectivamente que nome, idade e estado são
#pertencentes a cada um dos dados embutidos em uma tupla, então:
print(nome)
print(idade)
print(estado)
# porém se você não botar valores sufientes pode dar erro, como nesse exemplo em comentario:
# nome, idade = tuplaunpacking 
#vai dar erro pq a tupla tem 3 valores e não tem como a gente só 'desempacotar' 2 nesse exemplo, por isso tem como usar * para pegar alguns valores
#dentro dessas linhas, então vamos por exemplo:
tuplaunpacking2= (1,2,3,4,5,6,7,8,9,10)
ta , *te , ti = tuplaunpacking2
print (ta)#vai pegar o primeiro termo
print(te)# vai pegar todo termo que não foi selecionado/restante
print(ti)# vai pegar o ultimo termo

#ok, se ambos são praticamente iguais so mudam o fato de edição, porque/onde usar lista e typla?
#bom, existe uma diferença de 'peso' / 'tamanho' em que consome/gasta esses tipos de dados, então por exemplo:
import sys
lista = [0,1,2,'Hello',True] #repare que é o mesmo dado em lista e tupla
tupla = (0,1,2,'Hello',True)
print(sys.getsizeof(lista),"bytes") #104 bytes
print(sys.getsizeof(tupla),"bytes") # 80 bytes
#ou seja, lista são mais pesadas do que tupla, então usar tupla pode fazer seu programa ir mais rapido, demorar menos, travar menos e amenizar todos
#tipos de problemas causados por arquivos pesados
#para ficar mais visivel essa diferença:
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000)) #nesse codigo estamos pegando o tempo de criação do statement (stmt) 0 até 5 usando lista
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000))# e tupla, 1 milhao de vezes, e a diferença do tempo de criação dele é absurdo, demora 3
#vezes menos para criar statement de tupla doq de lista
#Dictionary 
#dictionary (traducao livre seria dicionario) usa parametro de {} para seu conteúdo, então há 2 formas de declarar dicionario:
#OBS: dictionary pode ser editavel, diferentemente da tupla
a = dict({'nome':'Alexandre','idade':20,'estado':'São Paulo'}) #assim como tupla, quando definimos typo como dict (tuple) e abre o parenteses(), devemos colocar dentro 
b = {'nome':'Nomequalquer','idade':34,'estado':'Minas Gerais'}# desses parenteses o sinal de dictionary que é as chaves {}
print(type(a))
print(a)
print(b)
print(type(b))
# em dicionario, o número a esquerda dos dois pontos ( : ) representa a palavra chave, então podemos usar dict para outro formato de dicionario:
c = dict(nome='Alexandre',idade=20,estado='São Paulo')
print(c)
#podemos também atribuir algum atributo para uma variavel usando a palavrta chave de um dicionario com index, então:
nomedict = c['nome']
idadedict = c['idade']
estadodict = c['estado']
print(nomedict)
print(idadedict)
print(estadodict)
#podemos adicionar items no dicionario usando lista, exmp:
c["email"] = "alexandre@htm.com"
print(c)
#a mesma coisa pode ser feita para alterar valores, então se eu declarar denovo essa palavra chave e mudar o valor dela, vai mudar na lista tmb
#como no exemplo abaixo:
c["email"] = "alexandreooliveira@htm.com"
print(c)
#OBs: esses valores so podem ser alterados se tiverem sidos adicionados depois, para alterar algum valor dentro de um dicionario usa outro metodo
#vou mostrar mais abaixo, por enquanto vamos ver para excluir:
#para excluir um elemento de um dicionario basta usar comando del, nome do dicionario e o valor q quer excluir, então:
del c['nome']
print(c)
#ou também podemos usar metodo .pop como no exmpl abaixo:
c.pop('idade')
print(c)
#apos o python 3.7 tem um novo comando que permite excluir o ultimo item inserido em um dicionario que é o metodo .popitem :
c.popitem()
print(c) # ele vai remover o ultimo termo que atualmente é o email, sobrando assim só o estado
#vou resetar a lista a partir desse ponto:
print('resetando lista =p')
c = dict(nome='Alexandre',idade=20,estado='São Paulo',email='alexandre@htm.com')
print(c)
#podemos verificar se tem um valor chave dentro de um dicionario, então podemos fazer com que:
if 'nome' in c:
    print(c['nome']) #vai fazer com que, se tiver o valor chave 'nome' no dict c, vai imprimir o nome equivalente à atribuição dele no dicionario
#a mesma coisa posso fazer com outros como:
if 'idade' in c:
    print(c['idade'])
if 'tamanho do pé' in c:
    print(c['tamanho do pé']) # nesse caso não existe, então não executara
# usando for loops em dicionarios:
print('-v- for loops -v-')
#for age de uma maneira diferente, os items de um dicionario se refere as chaves, então se eu digitar
for i in c:
    print(i) #vai printar todos valores chaves que possui o dicionario c, que no caso é 'nome','idade','estado','email'
#existe outra coisa que faz a mesma coisa que e usar metodo .keys():
for i in c.keys():
    print(i) # que diz a msm coisa, 'para cada elemento chave em c, print elemento'
#usando metodo .values() você pode puxar o elemento em si, então:
for i in c.values():
    print (i) #vai imprimir todos valores que contem uma chave no dicionario mencionado (que nesse caso é o c q leva o metodo c.values())
#podemos tambem ver a chave e o valor equivalente usando o metodo .items() junto com 2 valores no for, como no exemplo a seguir>
for i,c in c.items():
    print( i,c ) #sendo o primeiro item (i) a chave, e o segundo (c) o valor da chave
# existe um problema quando você copia qualquer coisa usando var1 = var2 que é, quando você modifica um os dois são modificados ao msm tempo, 
#se seu objetivo não for fazer isso, é melhor usar outros metodos como por exemplo:
#primeiro induzindo ao erro:
c = dict(nome='Alexandre',idade=20,estado='São Paulo',email='alexandre@htm.com')
c_copia = c
print(c_copia)
print(c)
print('Viu? mesma coisa, agora se nós adicionarmos um valor no c_copia vai adicionar no tmb: (obs: os dois print abaixo são usando respectivamente suas variaveis, c e c_copia)')
c_copia['tamanho do pé'] =42
print(c)
print(c_copia)
#para fazermos uma copia que não altere a outra, tem algumas principais maneiras de se fazer, como por exemplo:
c = dict(nome='Alexandre',idade=20,estado='São Paulo',email='alexandre@htm.com')
c_copia = c.copy() # que é usando o metodo copy, ou seja cria uma copia autenteica da variavel c, assim uma edicao em um não altera outro, como por exemplo:
print('usando .copy() :')
print(c_copia)
print(c)
print('depois de uma modificação:')
c_copia['tamanho do pé'] =42
print(c)
print(c_copia)
#outra maneira de se definir uma copia e usando a função (classe) dict, como abaixo:
c = dict(nome='Alexandre',idade=20,estado='São Paulo',email='alexandre@htm.com')
c_copia = dict(c)
print('usando funcao dict(c) :')
print(c_copia)
print(c)
print('depois de uma modificação:')
c_copia['tamanho do pé'] =42
print(c)
print(c_copia)
#essas são as duas formas de se copiar uma lista/dicionary/tupla
#agora sobre atualizar de dicionario:
dicionario1 = {'nome':'Alexandre','idade':20,'estado':'São Paulo'}
dicionario2 = dict(nome='Vanessa',idade=25,email='vanessa.@htm.com')
#agora vou atualizar os dados do meu dicionario1 com os dados do dicionario2 usando metodo .uptade()
print(dicionario1)
print(dicionario2)
dicionario1.update(dicionario2) #aqui acontece o seguinte, no dicionario1 e 2, tinham nome e idade, no 1 tinha estado q não tinha no 2, e no 2 tinha
#email q nao tinha no 1, então, ao dar uptade, todos valores chaves que possuem o mesmo, vai ser substituido, ou seja, nome e idade, vai ser substituidos
#pelo que esta dentro do paramentro do uptade [.uptade(parametro)], então o nome e idade foi alterado pelo dicionario2, agora, estado que tinha no
#1 e nao tinha no 2, ele continua lá com os dados do 1, e o email q tem no 2 e nao tem no 1, é adicionado nessa lista
print(dicionario1)
#OBS: para chamar um index de um dicionario é difernte de lista e tupla por exemplo q sao index 0 - x, index em dicionario é o valor da chave, então
#para chamar o index nome por exemplo, eu nao escreveria c[0] (já que o nome é o primeiro termo) e sim c['nome'], porém nada evita que eu use um número
#em dicionarios, então:
mesesdoano = {(1,13):'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
print(mesesdoano[1,13]) # vai imprimir o q contem o item chave 1 q é janeiro 
#no exemplo acima eu botei janeiro como uma tupla, então para chamar janeiro eu tenho que colocar o valor exato da tupla que é 1 e 13 separados por
#virgula
for i in mesesdoano.values():
    print(i)
#OBS: chaves em dicionario não podem ser alteradas, então uma vez que bote um valor, tem q permanecer esse valor, então, você pode usar uma tupla
#como valor de chave, porém não pode usar lista
# Set
#set é um valor de dado que usa a mestra estrutura de dicionarios(dict / dictionary), porém sem valores chaves, ele se comportará como uma lista
#porém não aceita valores duplicados, ele aceita apenas 1 valor de cada, então em um tipo set {1,2,3,1} print(set) ele printa só {1,2,3}
#sets são desordenados (ou seja, quando se bota em string, ele não tem ordem alfabetica, além de cada hora printar em ordem diferente
# , e por padrao, numeros inteiros nem sempre são ordenados de maneira certa),e são editaveis, diferente da tupla
meuset = {6,2,3,4,-2,1,3,1,6}
print(meuset)
meuset = set([1,2,56,4,4,3,2,10]) #para usar a classe 'set', dentro dos paremetros você tem que colocar os items como lista, como vimos em tupla,
#q a gente define tuple([]) igualmente
print(meuset)
meuset = set('Hello')
print(meuset)
#cuidado ao definir um set vazio, pois se você botar:
tiposet = {} #apenas entre colchetes, ele vai reconhecer como dicionario:
print(type(tiposet)) # saida = <class 'dict'>
#para você definir como um set, bote a classe set como no exemplo abaixo:
tiposet = set()
print(type(tiposet)) # saida = <class 'set'>
# como vimos, set pode ser 'mutavel' (editavel), então podemos adicionar items{english} dentro dele:
tiposet.add(1) #esse metodo permite apenas 1 adição por vez
tiposet.add(245)
tiposet.add(2)
tiposet.add(3)
tiposet.add(4)
tiposet.add(5)
print(tiposet)
#também podemos remover: .pop()
tiposet.pop() #diferentemente de lista, q pop excluir automaticamente o ultimo item, em set ele exclui o primeiro,
print(tiposet)
#também existe .remove()
tiposet.remove(3) # no parametro você bota qual valor quer remover, por exemplo está 3, vai remover o número 3 do set definido
"""tiposet.remove(100) # se tentarmos dar um valor que não existe dará erro (KeyError)
"""
print(tiposet)
#existe tmb .discard()
tiposet.discard(245) # a diferença entre esse e remove, é que se não encontrar o item para remover não dará erro, porém excluirá do mesmo jeito
tiposet.discard(1000)
print(tiposet)
#podemos também usar clear para limpar todos valores do set:
tiposet.clear()
print(tiposet)
#também podemos da mesma maneira em for loop's e if else q nem usamos lista, mas vou descrever exemplo abaixo:
meuset2 = {1,2,3,5,6,10,245,100}
for i in meuset2:
    print(i)
if 1 in meuset2:
    print("Tem")
#sobre união e intersecção de set:
impares = {0,1,3,5,7,9}
pares = {0,2,4,6,8}
primos = {2,3,5,7}
#para fazermos uniao basta usar .union(variavel set a ser adicionada)
numeros = pares.union(impares) # ou seja, union vai juntar dois sets sem aceitar duplicados, ou seja, botando 0 no impar por exemplo ele não repetirá o 0
print (numeros)
# podemos fazer intersecção para que mostre o que existe de igual em 2 sets diferentes, por exemplo:
num_iguais = impares.intersection(primos) # esse comando vai pegar tudo que tem no set impares e comparar com o set primos, o que tiver em 
#ambos set, vai ser o que retornara de saida
print(num_iguais)
num_iguais = impares.intersection(pares)# nesse caso a unica coisa q vai voltar é 0 pq eu botei em impar o 0, porém se não tivesse o dado de saida
#seria <set ()> pois  não tem valores em comum
print(num_iguais)
#Além de união e intersecção, podemos também fazer a comparacao de diferenças, entao por exemplo:
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diferenca = setA.difference(setB) # o que ficará armazenado na variavel diferença é os números q tem no setA e não tem no setB, ou seja, como 1,2,3
#tem em ambos, o valor q a variavel vai receber é o resto = 4,5,6,7,8,9
print(diferenca) 
# ao contrario ira inverter os valores sobre o qual se compara, e o output saida print seria 10,11,12:
diferenca = setB.difference(setA)
print(diferenca)
#existe outro metodo que irá pegar ambos conjuntos (set) e voltar o valor de todos números que não estejam em ambos das duas listas, ou seja, o valor
#de saida desse metodo seria 4,5,6,7,8,9,10,11,12:
diferenca = setA.symmetric_difference(setB)
print(diferenca)
#todos esses metodos precisa criar uma variavel para armazenar o valor separado pelo metodo, porém existe outro metodo que modifica o set em si
# que é o metodo .uptade() que vai pegar um conjunto set e dentro do parametro você coloca outra variavel de onde ele vai comparar os parametros,
#se esse parametro(set q fica dentro do parenteses) não existir no primeiro set (que irá usar o metodo), o set q usa o metodo irá copiar esses valores
# para si e se junto aos que ja existem, então se eu usar o comando:
setA.update(setB) # está dizendo q, o setA vai atualizar sua lista com todos items do setB, então, como ja tem o 1,2,3 e nao aceita duplicado, isso
#continua, no setA ja tem 4,5,6,7,8,9 eles vão se manter, e no setB q tem 10,11,12, vai passar uma copia desses valores para o A, então ficará:
print(setA) #setA ficará com todos valores embutidos, tanto o que ele já possuia tanto os que foi adicionado do setB
print(setB)# e o setB permanecerá com seus valores originais
# agora tem como a gente editar um set de acordo com algumas coisas, então por exemplo:
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.intersection_update(setB) #aqui está dizendo basicamente que: o setA vai se atualizar referente a intersecção do setB, ou seja, a variavel setA
#vai ser interseccao do item b, então atualmente antes dessa linha de codigo, o setA era 1,2,3,4,5,6,7,8,9 , depois desse comando, o setA vai passar
#a ter somente os valores se interseccao com o setB, ou seja, onde apenas os valroes são iguais, e como é so 1,2 e 3, o setA vai receber esses valores
print(setA)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.difference_update(setB)# esse funciona como o de cima porém ao contrário, setA agora vai começar a ter os valores que so tem no setA e não
#tem no setB, como por exemplo 4,5,6,7,8,9
print(setA)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.symmetric_difference_update(setB) # esse vai ser, o setA vai ignorar todos valores que possuam nos dois set e vai pegar todos que só existem 
#no setA e no setB, ou seja, 1,2,3 existem nas duas, estes serao ignorados, 4,5,6,7,8,9 só existe no setA, então ele será adicionado nessa nova
#definicao de dados do metodo, e 10,11,12 só existe no setB, então também será adicionado nessa nova definição de dados
print(setA)

setA = {1,2,3,4,5,6}
setB = {1,2,3}
#usando .issubset()
#metodo issubset() é uma pergunta do tipo 'é um subconjunto?',praticamente diz que por exemplo:
print(setA.issubset(setB)) # o conjunto setA é um subconjunto [ou seja, está dentro do conjunto] do conjunto setB?
# ele vai voltar valor verdadeiro ou falso, nesse caso seria o valor False pq setA é um conjunto que engloba o conjunto B e não vice versa, pois pensa
#comigo, o conjunto setA tem 1,2,3,4,5,6 e o conjunto b só tem 1,2,3 logo, para um conjunto engoblar um a outro ele tem que ser maior e possuir os 
#valores corespondentes
#porém se invertermos agora:
print(setB.issubset(setA)) # vai retonar verdadeiro, pois, além do setA ser maior q o B (sendo assim uma caracteristica minuscula{o sub}), todos valores
#do setB estão presentes no setA
#existe tmb metodo issuperset que é ao contrario, vai perguntar algo como: todos items do primeiro elemento possui os items do segundo? :
print(setA.issuperset(setB))#está perguntando se o conjunto setA é um 'superconjunto' de setB, q seria como, os items do setA possui todos elementos
#do conjunto setB? nesse caso ele voltaria verdadeiro (True)
print(setB.issuperset(setA))# e aqui pergunta, os items do setB possui todos elementos do setA? vai voltar falso(False) porque o setA existe valores
#q não estão no setB, como 4,5,6 e por exemplo
#existe o metodo para ver se eles são distintos, por exemplo:
print(setA.isdisjoint(setB))# vai retonar falso, pq pergunta, os items do setA são distintos de setB? por mais que existam 3 elementos q sejam, não
#são todos, e como existe 1 sequer, ele volta como falso,
#porém se eu criar um novo com valores distintos e fazer essa pergunta:
setC={7,8,9}
print(setA.isdisjoint(setC))# vai voltar verdadeiro, porque TODOS valores são distintos
#para fazer copias vai o mesmo erro e conceito de lista, então por exemplo, se eu fizer:
setA = {1,2,3,4,5,6}
setB = setA 
setB.add(10)
print(setA)# o valor a ser adicionado no B vai também para o A, fazendo assim perceber q isso não foi de fato uma cópia, porém se você quiser
print(setB)# de fato fazer uma cópia, você pode fazer de duas maneiras:
setA = {1,2,3,4,5,6}
setB = setA.copy() # essa é uma maneira
setB.add(10)
print(setA)
print(setB)
setA = {1,2,3,4,5,6}
setB = set(setA) # essa é outra, Ambas darão certa
setB.add(10)
print(setA)
print(setB)
#existe tmb o frozenset que é uma versão set porém imutavel, então por exemplo:
setimutavel = frozenset([1,2,3,4])
print(setimutavel)# ele fica como uma versão set porém sem permitir alteramentos q nem a forma padrao, então nao podemos adicionar nem excluir
#Strings:
#strins são tipo de dados em texto e para ser representado tem que estar dentro de aspas simples ou aspas duplas como por exemplo:
#'texto' ou "texto", e tem que tomar cuidado pois se você quiser usar alguma aspas dentro de uma string, vc tem que ter cuidado para que ela
#nao interfira, então existem 2 formas de tomar esse cuidado, o 1° é usar \', essa barra verificara que oq vc vai botar é um texto e nao um comando
# ou você pode por exemplo, se vai usar ' no meio da frase, você declara a string com "" ao inves de '', entao ao invés de botar ' texto \' aqui '
# você poderia botar " texto ' aqui "
#e existe print em varias linhas que seria triple quotation mark (aspas) [""""""]
minhastring = """Olá
Mundo 
Vasto
""" # ele considera até aqui, entao vai ser um espaço em branco q é nessa linha e ele exibira em linha como está, ou seja em uma linha será 'Olá',
#em outra será 'Mundo' e em outra será 'Vasto' e a ultima será um espaco em branco, para tirar esse espaço em branco eu deveria ter encerrado as
# aspas depois da mensagem Vasto e não botado na proxima linha q nem eu fiz (ou seja, eu deveria ter colocado as 3 aspas finais depois da palavra
# vasto na linha 522 e não na 523 q nem eu coloquei)
print(minhastring)
minhastring = """Olá    \
Mundo \
Vasto"""#da para reparar tmb q se colocarmos espaço depois da barra inversa (\) ele deixa de ser considerado um comando para nao quebra de linha e 
# se torna uma string, podendo ser imprimida por um input por exemplo
#podemos também usar o icone \ nesse contexto para especificarmos que não queremos que seja escrito em outra linha e sim na mesma linha

print(minhastring)
#modulos string
stringstrip = '                OLÁ você k         '
#o metodo .strip() tira todos espaço em branco no começo e no fim da string, porém como string não é mutavel, para fazer isso acontecer precisamos
#declarar uma cópia disso, então:
stringstrip = stringstrip.strip() #esse comando volta uma copia da string porém sem o espaço, se eu tivesse usado outro nome p variavel por 
#exemplo eu ainda conseguiria pegar o primeiro stringstrip com os espaços no começo e no fim
print(stringstrip) 
stringLstrip = '     olá mundo      ' # existem metodos que você bota o L na frente do metodo, eles indicam a direção, l para left e r para right
stringLstrip = stringLstrip.lstrip() 
print(stringLstrip,'Fica dificil visualizar, mas do lado direto da frase tem espaços pq foi so o lado esquerdo q tirou, esse texto estar mais p direita é a prova que esses espaços em branco existem')
minhastring = 'Olá, essa frase está inicialmente está apenas com o "o" de ola em maiusculo'
print(minhastring.upper(),'Agora usando o metodo .upper() que deixa tudo maiusculo')
print(minhastring.lower(),'.lower() que deixa tudo minusculo')
print(minhastring.title(),'.title() que deixa todas primeiras letras de cada palavra em maiuscula e o resto minuscula')
print(minhastring.capitalize(),'e agora .capitalize() que faz apenas a primeira letra da frase ser maiuscula, como já está isso então n vai fazer diferença visualmente')
print('Existem outras tags por exemplo usando a msms tags acima porem usando o is antes do upper/lower/capitalize/title que vai ser uma pergunta')
print('por exemplo: minhastring.islower() vai voltar valor boleano falso porque está perguntando se toda string de minhastring é minusculo')
print('porem se botar minhastring.iscapitalize() vai voltar valor boelano True pq ele está capitalizado (primeira letra maiuscula)')
# também podemos verificar se começa com uma letra especifica, como:
print(minhastring.lower().startswith('o')) # aqui fiz graça declarando como minusculo p voltar valor True, porem python diferencia letras maiusculas 
# e minusculas, então agora sem minha interferencia:
print(minhastring.startswith('o')) # volta False pq a primeira letra é 'O' maiúsculo e não minusculo
#porem isso nao serve so para uma letra e sim para o começo inteiro, por exemplo:
print(minhastring.startswith('Olá, e')) # isso volta True porque ele começa com essa sequencia, ou seja, não é so uma letra o parametro dele, é 
# 1 elemento, seja ele 1 letra ou 10.
# e existe o inverso de startswith que é endswith que é o mesmo conceito so que voltado para o final, então por exemplo:
print(minhastring.endswith('culo')) #volta valor True pq o final da minhastring é maiusculo
print(minhastring.endswith('CULO.'))# volta valor Falso pq o final é minusculo e não tem ponto final
# temos tmb o modulo find que vai voltar para voce o index daquela primeira aparição da palavra, então por exemplo, aparecem varias letras a,e,i na 
#minhastring, então vamos encontrar qual vai ser o primeiro 'o'(minusculo) que aparece
print(minhastring.find('o')) #esse valor me volta que é o index 47 o primeiro 'o' minusculo que aparece, agora vamos ver o ultimo, é usando
#o que eu mencionei acima que é botar 'r' de right = direita que ele vai procurar o valor mais a direita de o (que representa o final)
print(minhastring.rfind('o')) # e coeincidentemente me volta a posição 74 que está o último 'o' minusculo da minhastring
#tmb podemos usar isso para sequencia de letras tmb
print(minhastring.find('as')) # primeiro index de 'as' foi em 'frase' posição 12
print(minhastring.rfind('as'))# e o ultimo index de 'as' foi em 'apenas' posição 43
# se não tiver o que você botou dentro do paramentro em find() voltará o valor -1
print(minhastring.find('sopademacacocomcogumelo')) # voltou index -1
#tmb podemos contar usando o metodo .count(), por exemplo podemos contar quantas vezes o 'a' minusculo aparece na frase
print(minhastring.count('a'))#existe 7 'a' na frase, esse e o mesmo conceito do find e startswith, você pode botar uma frase ou uma letra dentro
#dos parametros do .count()
#se você quiser contar quantas letras a existem no total independente se for maiuscula ou minuscula você pode dar um .upper() e fazer a contagem
#com 'A' maior ou usar .lower() e usar a contagem com 'a' menor
print(minhastring.lower().count('o'))#esse comando transofmra tudo em minusculo dps procura
print(minhastring.count('o')+minhastring.count('O'))# ou você poderia fazer isso q você soma a qtde de 'o' minusculo e soma com a qtde de 'O' maiusculo
print(minhastring.count('o'))
#tambem podemos usar o modulo .replace() que vai alterar uma coisa por outra, por exemplo:
minhastring = 'academia de giraffa'
# minhastring é academia de giraffa, porém eu quero que se torne academia de urso, eu posso usar .replace( '#onde o primeiro parametro é oque
#você quer trocar', '#e o segundo e por qual você vai trocar' )
print(minhastring.replace('giraffa','urso')) # ele troca a palavra, se você colocar uma palavra q nao existe na string para trocar, ele nao reconhece
# e o print sairia normal (academia de giraffa)
# podemos tmb pegar uma string e separar todas frases delas em conteúdos q viram items de uma lista, por exemplo:
minhastring = 'essa sopa de macaco está sensacional'
minhastring2 = 'essa-sopa-de-macaco-está-sensacional'
minhalista = minhastring.split() # isso torna todos items de minhastring por items de lista separando onde tem espaço entre as letras,
minhalista2 = minhastring2.split()# porém podemos declarar onde queremos q ele quebre as palavras se botarmos em formato de string um valor nos 
#parametros dele, por exemplo esse comando acima desse jeito ele volta uma lista com apenas um item tudo junto pq ele n tem parametro e por padrao
#ele quebra nos espaços vazios porém eu nao deixei espaco vazio na minhastring2, eu botei - no lugar, entao para quebrar no - basta colocar ele de 
#parametro por exemplo:
minhalista3 = minhastring2.split('-')
print(minhalista)
print(minhalista2)
print(minhalista3)
#e podemos fazer algo parecido para juntar eles usando 'parametro'.join(lista q queremos juntar), entao por exemplo para juntar e voltar a ser a 
#minhalista1 para string dnv:
print(' '.join(minhalista))# esse metodo volta uma string formada, e a msm coisa para minhalista2:
print('-'.join(minhalista2))
from timeit import default_timer as timer
start = timer()
stringvazia = ''
for i in minhalista:
    stringvazia += i
stop = timer()
print(stop-start)
start = timer()
minhastring = ''.join(minhalista)
stop = timer()
print(stop-start)
# uma comparação do tempo que leva executar cada comando para juntar uma lista em string por exemplo, usar .join é mt mais eficiente
#formatando uma string: #existem 3 metodos, usando operador %, .format(), e f-string
#usando %
nome = 'Tom'
var = 'A variavel é %s' %nome #esse metodo junta já com a variavel acima usando %, a onde ela vai ficar no texto é representado com %s (provavelmente
#s de string) e a variavel é %nomedavariavel
# para juntar valores inteiros você usa dps da %d, então:
nome = 1
var = 'A variavel é %d' %nome # se você botar com s até vai tmb, porém vai definir que é uma string e nao um número
print(var)
# para juntar valores decimais use %f de float
nome = 1.234124214124 # quando usamos %f tmb podemos definir quantas casas dps do ponto pode aparecer q nem na f-string de print, então:
var = 'A variavel é %.2f' %nome # a unica diferenca é q n precisa usar :
print(var)
#porem esses metodos são todos antigos, f-string e .format() são mais novos que ja conhecemos que é:
nome = 'ola'
var = 'A variavel é {}' .format(nome)
print(var)
#tmb tem o msm sistema do float, e o lado bom é q n precisamos declara a variavel em si como antigamente, o python reconhece com base na variavel
nome = 1.21412542
var = 'A variavel é {:.1f}'.format(nome) # usando format você so pode editar tipo :.2f dentro das chaves da string onde fica azul:
#OBS> se tiver mais de uma variavel basta separar por virgulas no .format() e botar as chaves onde vai ficar a variavel na string
print(var)
# e usar f-string é oque já sabiamos tmb que é parecido com o .format() porém você n usa o .format(), você coloca tudo dentro das chaves apenas
#indicando antes do começo da string um f:
nome = 'olase'
var = f'A variavel é {nome}'
print(var)# e tem o msm esquema q ai sim pode botar tudo dentro das chaves q é :.2f para aparecer apenas 2 digitos dps do ponto e tudo mais..
#tmb podemos mexer com essas variaveis tipo:
var = f'A variavel é {nome * 2}'
print(var)#vai imprimir nome 2 vezes
#collections : é uma biblioteca ja inclusa no python naturalmente, vamos abordar sobre as principais: Counter, namedtuple, OrderedDict, defaultdict, deque
#_-----------------------------------------Sobre collections Counter -------------------------------------------------
from collections import Counter #counter ele vai voltar como formato dicionario onde vai ser as letras a keyword e a qtde de letras como parte vinculada
#entao por exemplo criamos uma variavel:
var = 'Esse é um teste para o counter, e agora adicionando números: 123,421,444'
print(Counter(var)) # a classe Counter está separando os elementos em um dictionary e me dizendo qts tem de cada um, ou seja, o espaço em branco ' '
#tem 11, ou seja, tem 11 espaço na string, 6 letras 'e' minuscula, 6 letras 'a' minuscula e por assim em diante, e você pode usar como dictionary
#ou seja, se você usar isso para definir uma nova variavel, essa variavel vai ser um dicionario q você consegue usar os mesmos modulos de dictionary
#como .keys(), .items() etc..
var1 = Counter(var)
print(var1.keys())
print(var1.items())
print(var1.values())
print(var1.most_common())# vai imprimir o que mais apareceu para o que menos apareceu da esquerda para direita
start = timer()
print(var1.most_common(1)) # aqui estou pegando o primeiro termo que mais apareceu, é importante ressaltar que aqui ele define o index0 como nulo,
print(var1.most_common(2)) #se botarmos 2 de parametro no most_common() não pegara o 2 mais digitado e sim os 2 primeiros mais digitado
stop = timer()
print(stop - start)
#para que possamos seguir a regra númerica de chamar o 1 da lista e nao o 0 por exemplo
start = timer()
print(var1.most_common()[0:2]) # desse jeito eu consigo pegar os dois primeiros termos mais usado, é uma forma alternativa
stop = timer()
print(stop - start)
# ATENÇÂO :: Agora q eu fiz o teste com timer() chego a conclusão que é mais eficiente você usar o most_common 2 vezes doq lista, é cerca de 7 vezes
#mais demorado p gerar se usar lista
#podemos tmb pegar o index de cada um daqueles que queremos no most_common, por exemplo:
print(var1.most_common(1)[0][0])#var1.most_common(1) até esse comando ele vai pegar o que mais apareceu
#..mmon(1)[0] esse index 0 se refere apenas uma confirmação do primeiro termo que é 1, ou seja, o valor q vc botar no parametro de common vc 
#tem que declarar o index dele, a não ser q você não declare ai você pode chamar pelo index que quiser
#..mmon(1)[0][0] e esse ultimo index 0 se refere ao valor q você quer pegar dentro dele, por exemplo em dictionary ele tem dois valores, o valor key
# e o valor value, por assim dizer, o index 0 se refere a chave e o index 1 se refere ao value, entao por exemplo nesse caso que o Count me traz um
#dic com a string e qts vezes ela apareceu, o index0 se refere a string e o index1 a qtde, nesse caso que eu escrevi me volta a string ' ' que é
#o espaço q mais apareceu
print(var1.most_common()[0][1]) # aqui eu n estou declarando o primeiro item, so to utilizadno o most common para organizar em ordem crescente
# e dps estou pegando o index 0 q é o q mais apareceu e dps o termo value do dictionary q é a qtde de vezes q aparece, q no caso vai imprimir 11
lista1 = ['ola','macaco','oq eu ia dizer msm?']
lista2 = ['mundo','sopa','e eu sei lá!']
lista3 = Counter(lista1 + lista2)
print(lista3) # mostrei q da p criar por lista tmb, porém funciona diferente, ele nao conta por caracteres e sim por item, então para q algum item 
#tenha 2 de vezes q aparece precisa estar escrito duas vezes, por exemplo: lista1 = ['ola','ola','ola'] o value da key = 'ola' daria 3 nesse caso...
#do mesmo jeito que transformamos em um dictionary tmb podemos voltar para uma string ou lista usando .elements()
print(var1.elements())# porém so esse comando volta ele em hexadecimal (eu acho kk tra escrito 0x00000235... se n me enganho x é hexadecimal, 0b é binario
# 0o é octal e tmb deve ter reclacionado a bytes e bits)
#para fazer isso precisamos transformar em lista
print(list(var1.elements()))#porém ele volta sem nenhuma ordem ou lógica, apenas retorna os valores, então a lista criada aqui tá tipo:
#['e','e','e','e','e','s','s','s','s','s','s','s','s',....]
# e tmb funciona com antigas listas para listas dnv, por exemplo:
print(list(lista3.elements())) # como so tinha 1 elenmto de cada ele acabou conseguindo voltar na ordem exata, porém quando se repete a ordem se quebra
#pq o comando faz voltar em ordem até qnd tiver uma repetida q vai eventualmente dps mostrar o valor repetido e dps continuar na ordem
#entao supor q a ordem era ('ola','mundo','ola','terra')
#ele volta ('ola','ola','mundo','terra')
#_-----------------------------------------Sobre collections namedtuple -------------------------------------------------
from collections import namedtuple
#primeiro passo é definir um elemento para namedtuple q em traducao livre é tupla nomeada que funciona da seguinte maneira:
point = namedtuple('point','x,y') # você declara namedtuple e dentro dos parametros você coloca no primeiro termo o nome da variavel q você declara para ela
# e o segundo valor é uma espécie de 'valor chave' parecido com  dictionary, ele vai voltar os parametros disso quando você declarar dps, por exemplo
# x vai ser o primeiro item da tupla e y o segundo, porém você nesse ponto deveria previamente já definir quantos elementos terá na tupla, se você
#quiser z por exemplo você deveria colocar tmb ja no parametro de namedtupla('point','x,y,z')
#logo após esses passos todo agora vem a parte q você de fato cria sua tupla: é quse como se você tivesse criado uma classe, agora na variavel
#vamos definir:
pt = point(1,10)#aqui definimos q a variavel pt vai ser igual a point(com parametros 1 , 10 respectivamente representando os lugares de x,y)
print(pt)
#agora podemos definir qual queremos ver, vamos ver o parametro y:
print(pt.y) # volta o valor q está representando o y que é o 10, parecido com dictionary
#_-----------------------------------------Sobre collections OrderedDict -------------------------------------------------
from collections import OrderedDict
#ordered dict é um dictionary padrao porém ele vai lembrar a ordem em que os items foi inserido, atualmente dps do python 3.7 ele ja tem a habilidade
#de fazer isso, porém para versoes menores você precisaria fazer desta forma
dicionario = OrderedDict()
dicionario['a'] = 1
dicionario['b'] = -1
dicionario ['c'] = 2 #aqui vai lembrar a ordem de inserimento q vai mostrar em ordem a = 1, b = -1 e c = 2
print(dicionario)
#_-----------------------------------------Sobre collections defaultdict -------------------------------------------------
from collections import defaultdict
#esse é você bota um valor padrao para o dicionario quando ele nao acha o item, por exemplo:
f = defaultdict(int)#se eu declaro q o padrao é int, se ele nao achar o item ele vai imprimir 0
i = defaultdict(float)# padrao float: 0.0
print(f[0])
print(i[0])
l = defaultdict(list)#aqui ele reconhece valor padrao de []
#sem usar o default, quando procurar algum valor que ele não encontre ele dará keyerror0, usar default pode ser bom para não parar programas
"""
dictsemdefault = {}
print(dictsemdefault[0])
"""
#_-----------------------------------------Sobre collections deque -------------------------------------------------
from collections import deque
#deque é uma especie de lista porém um pouco mais dinamica, você consegue adicionar e remover itens à esquerda #basta imaginar em um deck d cartas
#como se você tivesse com elas espalhadas na mão...
d = deque()
d.append('ola')
d.append('mundo')
d.append('Como')
d.appendleft('ei!') # adicionamos 'ei!' ao lado esquerdo do 'deque', e podemos fazer o mesmo com .pop()
d.popleft()#vai remover o item da esquerda
d.pop()#vai remover o item da direita de maneira padrão q nem funciona com lista
print(d)
# podemos usar .clear p limpar tmb:
print(d.clear())#são funcionalidades de lista porém com left em alguns casos
# e tmb podemos acrescentar uma lista em outra:
d.extend([1,2,3,4,5,6,7])
print(d)
d.extendleft([0,-1,-2,-3,-4])# e tmb podemos usar extend para acrescentar à esquerda, porém ele acrescenta de forma que os items da direita do extend
#fiquem ao lado mais esquerdo da lista d como vemos no print abaixo:
print(d)
#usando .rotate() os parametros q rotate aceita sao numeros inteiros que vai 'girar' os elementos 1 casa para direita, veja:
d.rotate(1) # a lista vai ficar 7,-4,-3,-2,-1... o 1 de parametro é quantas casas p direita cada elemento vai andar
print(d)
d.rotate(2)# agora vai andar 2 casas p direita cada numero, eles ja foram alterados pelo d.rotate(1) de cima entao agr andando mais 2 vai ficar:
#5,6,7,-4,-3,-2,-1...
print(d)
#----------------------------------------------------------ITERTOOLS-------------------------------------------------------------------------------
#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
#itertools é uma biblioteca inata do python, então devemos primeiramente importa-lá
#_______________________________________________________ITERTOOLS PRODUCT__________________________________________________________________________
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(prod)# ele está como um iterator object (0x0000022A1B1A1740) (iterator é uma espécie de conteiner que o programa consegue acessar para pegar 
#os dados) para convertermos isso vamos converter em formato de lista:
print(list(prod)) # ele volta uma combinacao de (a[0] com b[0]) e (a[0] com b[1]) e depois de a[1] com b[0] e [1] respectivamente,
#podemos colocar para repetir tmb:
prod = list(product(a,b, repeat = 2)) # aqui ele vai funcionar como se fosse um for loop, vai juntar 1,3 e dps vai 'repetir' o laço para
#o segundo termo denovo que vai começar tmb em 1,3, ai dps vai começar a fazer a msm comparacao mantendo os 2 primeiros e criando a combinacao dos 
#dois ultimos, bem complicado mas imagine numeros (1,2) e (3,4)
#ele vai comecar juntando (1,3),(1,4),(2,3),(2,4), quando declaramos repeat é para repetir essa logica dentro dessa tupla criada internamente
#entao fica (1,3,1,3),(1,3,1,4)....
#para facilitar a compreensao vamos supor os mesmos numeros:
#([0][0]) eles comecam nessa combinação, ai dps ele muda e vira ([0][1]), dps ([0][2] e por final ([0],[4]) ante se finalmente tornar ([1][0]) e por 
#assim adiante ate o final) 
print (prod)
#_______________________________________________________ITERTOOLS PERMUTATION______________________________________________________________________
from itertools import permutations
#permutation funciona para mostrar os items em toda sequencia possivel, então:
a = [1,2,3]
print('permutacao abaixo (tá mt junto do product feito acima ai fica dificil visualizar :c)')
perm = permutations(a) #aqui ele volta um iterator object, para converter novamente usando lista:
print(list(perm)) # e nesse print vai aparecer todas possiveis permutacoes (trocas) de itens dentro da ordem ou seja, 1,2,3 podem ficar tmb 
#nas seguintes posições: (conteudo do print)
#tambem podemos diminuir a largura disso, então vamos supor que eu quero ver todas opções porém de apenas 2 digitos: basta colocar virgula e esse 
#valor dentro do parametro:
perm = permutations(a,2)
print(list(perm)) #aqui ta imprimindo todas possiveis combinações com 2 items dentro da variavel perm que está pegando a variavel a
#_______________________________________________________ITERTOOLS COMBINATIONS______________________________________________________________________
from itertools import combinations
#combinations tem um mesmo padrao de parametro e convertimento que permutation, que é colocar list() para transformar e dps os parametros que o 
#primeiro é a variavel e o segundo é a 'largura' das combinações...
# combinations ele vai combinar todos possiveis valores, ou seja ele não vai aceitar items repetidos apenas alterando a ordem, então os numeros 
#1,2,3 viram apenas 1,2 , 1,3 e 2,3. Já que 3,1 por exemplo são os mesmos valores que 1,3 porém invertido, coisa que o combination já não aceita
a = [1,2,3]
print('Itertools combinations abaixo vvvv')
comb = combinations(a,2)
print(list(comb))
# tambem existe combinations_with replacement 
from itertools import combinations_with_replacement
#combinations_with replacement é combinations soq com repeticao, entao no exemplo de 1,2,3, ele vai imprimir 1 de cada estilo, ou seja, 
#1,1 1,2 1,3 2,2 2,3 / note que não existe o 2,1, pq como ele é igual ao combinations, 2,1 seria o mesmo valor que 1,2 invertido vvv
combwr = combinations_with_replacement(a,2)# segue o mesmo parametro de largura
print(list(combwr))
#_______________________________________________________ITERTOOLS ACUMULATE________________________________________________________________________
from itertools import accumulate
#accumulate funcion funciona por exemplo você tem uma lista:
lista = [1,2,3,4]
acum = accumulate(lista)# aqui estou declarando que ela está acumulando, por padrao ela soma, então vai funcionar assim:
#essa classe é q nem as outras acima, precisamos converter para lista, mas oq ele vai fazer é q vai somar os itens, então ele vai sair a soma
#dos itens em uma lista, de exemplo eu dei 1,2,3,4 ou seja, a lista q ele retorna p mim é: o primeiro número é 1, o segundo número, é ele + o anterior
# q vai ser 1+2 entao o segundo número vira 3, o 3° numero vira ele +  anterior, que virou 3, então 3 + 3 = 6 e o 4° número vai ser o item 4 da lista
# + o anterior que virou 6, então 4+6 = 10
print(list(acum))
#vamos alterar os valores, vamos botar lista como 2,4,6, e 10
lista = [2,4,6,10]
acum = accumulate(lista)
print(list(acum)) #vai voltar o 1 em: 2, o 2° em: 4 + 2 = 6, o 3° em 6 + 6 = 12, e o 4° em: 10 + 12 = 22
# por padrao é soma, porém tambem podemos multiplicar, para isso precisaremos importar a biblioteca operator
import operator
# e agora devemos definir com operator para multiplicar, então:
acum = accumulate(lista, func=operator.mul)
print(list(acum)) #aqui ele está multiplicando todos items da lista usando o operator.mul
#também podemos usar outra func no operador para que ele compare sempre o 'maior' usando a func = max
#para funcionar melhor vou trocar a lista por: 
lista = [1,4,7,5,3,8,2,1,4,5,2]
acum = accumulate(lista, func = max) # max nao precisa immportar
print(list(acum)) # usando o max ele vai imprimir os números na ordem, porém ele vai comparando, então 1,4 o 4 é maior ok, 4 e 7, o 7 é maior ok,
# 7 e 5, o 7 é maior então usa o maior (max) e print o 7, ignore o menor, 7 e maior q 3, imprime o maior (7)e esquece o menor, 8 é maior entao ignora
#o 7 e imprime o 8, 8 maior q 2 entao imprime o 8 e ignora o 2...
#_______________________________________________________ITERTOOLS GROUPBY_________________________________________________________________________
from itertools import groupby
#em groupby você faz um agrupamento por lambda function ou por function direto que retorna duas listas sobre verdadeiro e falso, para isso vamos usar:
#primeiramente declarar uma variavel q contenha a classe groupby
lista = [1,2,3,4,5,6,7,8,9]
def menorque4(x):
    return x <= 4
gb = groupby(lista,key=menorque4) #para chave aqui devemos definir uma função que faça o que queremos e volte um valor booleano, então vou criar na linha
#acima uma funcao q volta se o número é menor ou igual a 4:
# pronto, agora criado agora eu vou botar no parametro da 'key' o nome da minha funcao:
#agora vamos imprimir: 
print(gb) # ele está imprimindo o inter object dele, agora para fazermos acontecer precisamos começar a separar e comparar todos items da lista 
#usando um for loop
for key, value in gb:
    print(key, list(value)) # ou seja, ele vai compara cada item da lista na função que definimos em groupby que é menorque4 q vai voltar falso ou
    #verdadeiro para a expressao x <= 4, poderia fazer outras combinações tmb, então aqui no for, estou dizendo que: para chave e valor na variavel gb
    #me mostre na tela a chave (que no caso so pode ser verdadeira e falso pq é o que retorna da funcao menorque4) e os valores eu converto em 
    #lista para poder visualizar, os valores vai ser correspondente a tipo, se a chave de 9 é false, ele vai se englobar na chave false, por exemplo
    #na comparacao vai fazer, 1 < 4? True, então o 1 volta valor True, como True é oq volta da função, ele é nossa chave (key) e o parametro que 
    #comparamos (x <= 4), o x que voltou o valor da expressao vira nosso valor (value)
#vamos fazer algo que separe os impares dos pares:
def impar_ou_par(x):
    return x % 2 == 1
lista=[1,2,3,4,5,6,7,8,9,0,12,145,136637,12345,124]
gp1 = groupby(lista, key=impar_ou_par)
for key, value in gp1:
    print(key, list(value)) # aqui ele está imprimindo verdadeiro para os impares e falso para par, ele vira uma lista enorme pq ele faz comparacao de 1 -1, então
    #se da impar, vira True, se o prox par, e outra linha escrita False, no 3 q é impar dnv ele nao fica junto com 1 que é True, pq ele ja imprimiu
    #o 2 false antes, então ele cria outra linha
 # podemos tmb usar lambda # vai ser explicado com mais detalhe no proximo topico daqui, porem para adiantar é fazer uma funcao em 1 linha:
"""
OBS::: EU NAO SABIA NA HORA QUE ESTAVA FAZENDO ISSO MAS TEM OUTRA FORMA DE FAZER ISSO AQUI MELHOR, BASTA USAR SUBMODULO FILTER DE LAMBADA QUE
EU EXPLICO MAIS ABAIXO VVVVVV SE ORIENTE PELAS UNDERLINES QUE EU BOTEI COM SEUS RESPECTIVOS CONTEUDO
"""
lista = [1,2,3,4]
gp2 = groupby(lista,key=lambda x: x==3)#aqui funciona da msm maneira de definir uma variavel, a gente substitui a 'key' por lambda e escreve na 
#frente seus parametros (que nesse caso é representado pelo 'x' antes dos dois pontos ':') e na frente dos dois pontos a gente bota o que deve fazer
# que nesse caso está comparando se x é igual a 3, ou seja, vai voltar 1 valor true e 3 false:
for key,value in gp2:
    print(key,list(value))
pessoas = [{'Nome':'Alexandre','Idade':21},{'Nome' : 'Icaro','Idade':21},{'Nome':'Marcos','Idade':29}]
gppes = groupby(pessoas,key=lambda x : x['Idade']) # aqui vai retornar o x que é a sequencia inteira de nome nome idade numero e dps vai retornar 
#o value da chave 'Idade': #obs>: mesmo sem estar escrito, oq vem dp´s dos : significa algo como return x ['Idade']
for key, values in gppes:
    print(key,list(values))# como está seguido, ele me volta todos valores q estão juntos, então ele me retorna 21 e o 'x' que é nome:alexandre
    #idade : 21 e o nome:icaro,idade:21 porque ele tmb é 21, ou seja, a chave aqui é 21, não chega nem a ser valor boleano
#_______________________________________________ITERTOOLS COUNT,REPEAT, CYCLE_________________________________________________________________________
#ASSIMc como outros precisamos importar:
from itertools import count,repeat,cycle
#são simples como por exemplo:
"""
for i in count(): #GERA UM LOOP INFINITO CONTANDO DO VALOR Q VOCÊ BOTAR NO PRIMEIRO PARAMETRO PULANDO DE 1 EM 1,
    print(i)      # você pode acabar botando os 'steps' dele para fazer ele pular de x em x números,
#por exemplo:
for i in count(10,2):
    print(i)         #aqui ele vai ccomeçar um loop infinito comecando do 10 e pulando de 2 em 2, ou seja vai imprimir:
    12,14,16,18..infinitamente
    #para parar esse loob basta colocar uma condicao (if) e break onde vc quer parar, entao:
"""
for i in count(10,2):
    print(i)
    if i == 20:
        break

#cycle vai repetir os parametros infinitamente, então por exemplo tenho uma lista com:
lista =[1,4,7,10]
""" # e faco:
for i in cycle(lista):
    print(i)
    #vai imprimir uma sequencia infinita de repeticoes da variavel lista, entao:
    1,4,7,10,1,4,7,10,1,4,7,10,1,4,7,10,1..... infinitamente
"""
#repeat ele vai repetir um mesmo número e ele tem o parametro de parar, então por exemplo:
for i in repeat('a',5): #o primeiro parametro é qual você quer imprimir infinitamente, o segundo parametro tira a infinidade e bota um limite 
    #so aceita números inteiros no segundo parametro, ou seja, nesse caso vai imprimir 'a' 5 vezes
    print(i)
#_______________________________________________LAMBDA FUNCTION_________________________________________________________________________
# lambda é uma funcao de 1 linha que nao ganha nome e serve para um determinado proposito dentro da sua linha de codigo, como usei no exemplo
#acima como parametro de key= para uma classe
#por exemplo criar uma variavel q leva lambda em si:
add10 = lambda x: x+10
print(add10(10))# usando add10 uma variavel contendo ele, a gente consegue usar lambda como uma funcao sem definir um nome para ela
#podemos tmb definir lambda com mais de um valor
mult = lambda x,y: x*y
print(mult(2,4)) #volta expressao 8
#lambda é usado quando você precisa de uma funcao curta
#tambem podemos usar para outras coisas como por exemplo sorted em lista q organiza, por exemplo:
lista =[(1,2),(3,-1),(10,4),(5,2)]
lista = sorted(lista) # usando esse comando ele vai organizar a lista em formato crescente a partir do index 0 de cada tupla
print(lista)# porem com lambda podemos mudar isso:
lista =[(1,2),(3,-1),(10,4),(5,2)]
lista = sorted(lista,key=lambda x: x[1])
print(lista) # e agora ele fica organizado de ordem crescente em relação ao index 1, comparare no print para melhor entendimento
#outro exemplo, vamos organizar (sort) de maneira para a soma dos elementos:
lista =[(1,2),(3,-1),(10,4),(5,2)]
lista = sorted(lista,key=lambda x: x[0]+x[1]) # aqui vai voltar as tuplas em ordem da soma delas, no caso 3 + (-1) = 2, oq e o menor número entaõ ele
#aparece primeiro, dps 1 + 2 =3, aparece em 2°, dps vem 5+2 =7 que aparece em terceiro e por ultimo 10+4 = 14 q aparece por ultimo
print(lista)
#                      uso de lambda              _______MAP_______
#map(func,seq)
#vamos supor que temos uma lista 1,2,3,4,5:
lista = [1,2,3,4,5]
print(lista)
# e agora queremos outra lista q mostre p nos o dobro dessa primeira por exemplo, podemos usar o map:
listaM2 = map(lambda x: x*2,lista) # primeiro colocamos a funcao que é sobre o lambda dps separamos por uma virgula qual variavel ele vai pegar para
# executar a lambda function
print(listaM2) # ele volta como objeto, precisamos converte-lo para lista também
print(list(listaM2))#e aqui ele volta uma lista usando a funcao q declaramos no map
# porem isso é parecido com oq vimos anteriormente aqui que é usando list comprehension syntax que é:
listaM2list = [x * 2 for x in lista]
print(listaM2list)
#                      usos de lambda              _______filter_______
#filter(func,seq) # nesse uso a funcao que for usada DEVE voltar apenas valores boleanos, ou seja, True ou False
#vamos criar separador de impares e pares por exemplo:
listaparaseparar = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,124,156,1246574,12342563748463455634,634653456435733,3634]
separador = filter(lambda x: x%2==0,listaparaseparar)
print(separador)# é preciso converter para lista
print(list(separador)) # ele voltara os valores em uma lista de todos que sejam True para a equacao em lambda q fizemos
# porém também podemos usar compreensao de lista para fazer isso:
separadorlista = [x for x in listaparaseparar if x%2==0]
print(separadorlista)
#                      usos de lambda              _______reduce_______
#precisamos importar
from functools import reduce
# reduce(func,seq)
# reduce vai voltar algo em 1 so argumento, por exemplo a listaparaseparar acima, vamos somar todos items dela e transformar em apenas 1 argumento
#somado, entao:
somaLPS = reduce(lambda x,y:x+y,listaparaseparar)# precisa de 2 argumentos no lambda, aqui estou dizendo para ele somar todos items da lista
#usando algo como: x + y, o y aqui sendo representado pelo proximo item da lista e dps declaramos que ele vai pegar os argumentos da variavel listaparaseparar
print(somaLPS)
#________________________________________________________TRY , EXCEPCTION _________________________________________________________________________
#try e except usa para indicar algum erro que deu no programa sem que pare ele, entao por exemplo:
try:
    a = int(5/0) #ele vai tentar esse comando, se der erro
except:
   a =  int(5/1) # ele faz isso, nesse caso parece um if, porém essa é uma das formas de fazer isso
print(a)
try:
    a = 5/0
except Exception as varqualquer: # aqui estou falando que se der errado no bloco try acima, ele vai aparecer a mensagem doque aconteceu de erro
    print(varqualquer)# (exception) e eu guardei essa msg de erro na minha variavel varqualquer para poder imprimir que volta na tela output que
    #o erro é divisionbyzero
#porem podemos nos atentar para algo em especifico que ocorra, por exemplo se caso o erro que de for divisionbyzero por exemplo podemos ja declarar
    #no nosso bloco de except:
try: 
    a=5/0
except ZeroDivisionError:# percebe q e uma classe que nem o Exception encima q fica verde tmb, e esse except so vai acontecer se o erro de cima 
#for erro de zerodivisionerror, caso for outra coisa tipo keyvalue nao vai atracar aqui pq esse ESPECIFICA CLARAMENTE que é sobre o erro zerodivision
    print('Impossivel divisão por zero')
"""
#entao vamos tentar dnv agora fazendo outro erro e deixando except como zerodivision:
try:
    a=5/0
except KeyError:
    print('Você digitou algo errado porém nao foi divisão por 0 entao eu vou ignorar :) ')
# MEU PROGRAMA ENCERRA AQUI COM MENSAGEM DE ERRO, PQ COMO HOUVE UM ERRO DE DIVISAO POR 0 POREM NAO TEVE O EXCEPT CORRETO PARA BARRAR ESSE ERRO
#MEU PROGRAMA CONTINUA COM ELE E QUANDO SAI DO BLOCO DE EXCEPT P CONTINUAR O PROGRAMA ELE PERCEBE QUE O ERRO CONTINUA E NAO FOI BOTADO UM PARAMETRO
#PARA QUE ELE CONTINUASSE MSM COM ERRO ENTAO ELE ENCERRA
"""
#PODEMOS USAR VARIOS EXCEPT PARA UM TRY, POR EXEMPLO:
try:
    print('ola')
    e = 1 + 2
    e = "Sopa"
    print('Vai ter um erro nesse comando que vai ter um index nao existente no final dessa linha de comando',e[2])
except ZeroDivisionError:
    print('Impossivel divisao por zero')
except IndexError as a:
    print('Não existe esse termo index no comando especificado',a)
except Exception as a:
    print('Não foi possivel realizar seu programa por conta do erro:',a)
# tambem podemos botar um else para indicar que tudo ocorreu bem:
else:
    print('Não ocorreu erros na execução')
# e tambem tem o finally que vai acontecer independente se o programa der certo ou errado:
finally:
    print('Limpando dados para nova execução...')
"""
# também podemos criar nossa propria exception para indicar um erro, por exemplo:
class ValueToHighError(Exception):
    pass
def teste_valor(x):
    if x > 100:
        raise ValueToHighError('Valor muito alto, encerrando programa')
teste_valor(200)
"""
#também podemos definir nossa própria mensagem de erro com o valor do erro, por exemplo:
class muitopequeno(Exception):
    def __init__(self, mensagem, valor):
        self.mensagem = mensagem
        self.valor = valor
    
class ValueToHighError(Exception):
    pass
def teste_valor(x):
    if x > 100:
        raise  ValueToHighError('Valor muito Alto')
    if x < 5:
        raise muitopequeno('Valor muito pequeno', x) # pegando o valor do erro aqui por exemplo porem lembrando da criacao da class muitopequeno
#para fazer isso funcionar embaixo tmb, emcima eu declarei q ele recebe dois parametros chamado mensagem e valor, então a ordem importa para 
#que o python consiga reconhecer quem e quem por assim dizer, nesse caso está apenas imprimindo porém está ai
try: 
    teste_valor(1)
except ValueToHighError as e:
    print(e)
except muitopequeno as e:
    print(e.mensagem, e.valor)
#________________________________________________________LOGGING _________________________________________________________________________
#python ja tem um bom modulo de logging (Um log de alterações é um arquivo que contém um registro cronológico das alterações feitas no software)
#basta apenas importar
import logging
"""
logging.debug('Debug mensage')
logging.info('Info mensage')
logging.warning('Warning mensage')
logging.error('Error mensage')
logging.critical('Critical mensage')
"""
# ao printarmos esses comandos, aparece mensagem apenas de logging.warning para baixo, isso é por conta da configuração padrao do módulo, para
# mudarmos isso precisamos acessar a configuracao com o comando:
logging.basicConfig(level=logging.DEBUG,format ='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S',
)#filename='logtestepython.log')
logging.debug('Debug mensage')
logging.info('Info mensage')
logging.warning('Warning mensage')
logging.error('Error mensage')
logging.critical('Critical mensage')
"""
# esses logging são por padrao e podemos editar algumas coisas nele como mostrando no logging.basicConfig() porém tmb podemos criar nosso proprio 
#logger especifico:
log = logging.getLogger(__name__) # é uma boa prática você usar a variavel __name__ como nome, assim o logging é criado com o mesmo nome do módulo
#que vai ser nesse caso: o nome do arquivo q é 'sequenciaparaestudo2', entao imagina um import q precisariamos dar tipo sequenciaparaestudo2.log('msg')
#eu vou criar esse log em outro arquivo:
"""
import createlog
# do jeito que está agora ele assim que é importado ele já da um primeiro logger, para remover isso basta colocar a propriedade no nosso arquivo:
#var.propagate = False
#existe tmb o manipulador (handler) que dá para usar no log para que certas msgs se direcionem para algum lugar especifico, verificar esse estudo
#na pasta 'createlog.py'

