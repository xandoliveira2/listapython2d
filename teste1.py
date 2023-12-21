from estudantesclasse import perguntas
questoes = [
"Qual a cor da banana?\n(a)Amarela\n(b)Vermelha\n(c)Roxa\nr: ",
"Qual a cor da maçã?\n(a)Amarelo\n(b)Vermelho\n(c)Roxo\nr: ",
"Qual a cor da ameixa?\n(a)Amarelo\n(b)Vermelho\n(c)Roxo\nr: ",
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
respostas (listaresposta)