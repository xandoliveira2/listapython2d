class estudantes:#comece com class e depois o nome que você vai dar para essa classe seguida com :
    def __init__(self,nome,nomecurso,notamedia,matriculado ):#estou declarando que o __init__ que é initialize (inicializar) estou declarando que 
#começando a declarar no caso né que a class estudantes possui nome(str), ano(int), notamedia(float), matriculado(bolean), estou declarando que
#estudantes possui essas 4 formas de dados##esse valor self pode ser alterado por qualquer q voce quiser, ele é uma variavel para atribuir outros valores
        self.nome = nome
        self.nomecurso = nomecurso
        self.notamedia = notamedia
        self.matriculado = matriculado

class motorista:
    def __init__(self,nome,tipodehabilitacao):
        self.nome = nome
        self.tipodehabilitacao = tipodehabilitacao
class fruta:
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
class perguntas:
    def __init__(self,comando,resposta):
        self.comando = comando
        self.resposta = resposta
class question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer
class estudantes1:
    def __init__(self,nome,nomecurso,notamedia):
        self.nome = nome
        self.nomecurso = nomecurso
        self.notamedia = notamedia
    def elite(self):
        if self.notamedia >= 6:
            return True
        else:
            return False
class chefe:
    def fazeralmoco(self):
        print('Preparar almoço')
    def fazercafedamanha(self):
        print('Preparar café da manha')
    def fazerjanta(self):
        print('fazer janta')
"""
class chefechines: 
    def fazeralmoco(self):                         esse metodo foi feito copiando e colando, dá muito trabalho e as vezes pode ser mt trabalhoso,
        print('Preparar almoço')                por isso existe como herdar de classes:
    def fazercafedamanha(self):                 
        print('Preparar café da manha')          
    def janta(self):                              
        print('fazer janta com arroz frito')        
    def sobremesa(self):                        
        print('preparar bolo de chocolate')          
        """
#para começar a herdar, caso o arquivo não esteja aqui, precisamos importar, como ja tá (que é a classe chefe) não vamos importar, mas caso esteja
#fora do arquivo a gente precisa dar 'from nomedoarquivo import nomeclasse'
class chefechines(chefe):#para herdar basta colocar entre parenteses o nome da classe q você quer herdar 
    def fazerjanta(self):
        print('fazer janta com arroz frito')
    def fazersobremesa(self):
        print('preparar bolo de chocolate') #nesse caso herdamos todos pratos do chefe, e adicionamos a mais fazer sobremesa, porém ainda precisamos
#editar o prato de janta que é diferente do chefe, nesse caso nao tem muito o que fazer, você re-escreve a funcao e altera oq tem q alterar