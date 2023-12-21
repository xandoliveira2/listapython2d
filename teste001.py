camposprint = [
          ['A1','B1','C1','D1','E1','F1','G1','H1'],
          ['A2','B2','C2','D2','E2','F2','G2','H2'],
          ['A3','B3','C3','D3','E3','F3','G3','H3'],
          ['A4','B4','C4','D4','E4','F4','G4','H4'],
          ['A5','B5','C5','D5','E5','F5','G5','H5'],
          ['A6','B6','C6','D6','E6','F6','G6','H6'],
          ['A7','B7','C7','D7','E7','F7','G7','H7'],
          ['A8','B8','C8','D8','E8','F8','G8','H8'],
          ]
campos = ['A1','B1','C1','D1','E1','F1','G1','H1',
          'A2','B2','C2','D2','E2','F2','G2','H2',
          'A3','B3','C3','D3','E3','F3','G3','H3',
          'A4','B4','C4','D4','E4','F4','G4','H4',
          'A5','B5','C5','D5','E5','F5','G5','H5',
          'A6','B6','C6','D6','E6','F6','G6','H6',
          'A7','B7','C7','D7','E7','F7','G7','H7',
          'A8','B8','C8','D8','E8','F8','G8','H8',
          ]
import random
navios = random.choices(campos,k=8)
print(navios)
for i in camposprint:
    for c in i:
        print(i.index(c))

""" copia p caso eu faça merda na outra kk
#batalha naval? teste1 tentando criar interface de 8 x 8
import random
campos = ['A1','B1','C1','D1','E1','F1','G1','H1',
          'A2','B2','C2','D2','E2','F2','G2','H2',
          'A3','B3','C3','D3','E3','F3','G3','H3',
          'A4','B4','C4','D4','E4','F4','G4','H4',
          'A5','B5','C5','D5','E5','F5','G5','H5',
          'A6','B6','C6','D6','E6','F6','G6','H6',
          'A7','B7','C7','D7','E7','F7','G7','H7',
          'A8','B8','C8','D8','E8','F8','G8','H8',
          ]
camposprint = [
          ['A1','B1','C1','D1','E1','F1','G1','H1'],
          ['A2','B2','C2','D2','E2','F2','G2','H2'],
          ['A3','B3','C3','D3','E3','F3','G3','H3'],
          ['A4','B4','C4','D4','E4','F4','G4','H4'],
          ['A5','B5','C5','D5','E5','F5','G5','H5'],
          ['A6','B6','C6','D6','E6','F6','G6','H6'],
          ['A7','B7','C7','D7','E7','F7','G7','H7'],
          ['A8','B8','C8','D8','E8','F8','G8','H8'],
          ]
navios = list(random.choices(campos,k=8)) #h1 f2 h1 d3 b6 f1 e3 f8
if navios[0] == navios[1] or navios[0] == navios[2] or navios[0] == navios[3] or navios[0] == navios[4] or navios[0] == navios[5] or navios[0] == navios[6] or navios[0] == navios[7] or navios[1] == navios[2] or navios[1] == navios[3] or navios[1] == navios[4] or navios[1] == navios[5] or navios[1] == navios[6] or navios[1] == navios[7] or navios[2] == navios[3] or navios[2] == navios[4] or navios[2] == navios[5] or navios[2] == navios[6] or navios[2] == navios[7] or navios[3] == navios[4] or navios[3] == navios[5] or navios[3] == navios[6] or navios[3] == navios[7] or navios[4] == navios[5] or navios[4] == navios[6] or navios[4] == navios[7] or navios[5] == navios[6] or navios[5] == navios[7] or navios[6] == navios[7]:
    print('Erro, favor reiniciar programa')
    quit()            


print (navios)
for i in camposprint:
    print(i)
embarcacoes = 7
while embarcacoes != -1:
    tiro = str(input('Digite um campo para atirar: '))
    
    
    if tiro.lower() in ',.;':
        break
    if tiro.upper() in navios:
         print(f'Você acertou \n restam ainda {embarcacoes} embarcações')
         embarcacoes -= 1
         for i in camposprint:
             for c in i:
                if c == tiro.upper():
                   camposprint[camposprint.index(i)][i.index(c)] = 'X'              
    elif tiro.upper() != navios:
        for i in camposprint

        print('voce errou, tente novamente')

    for i in camposprint:
        print(i)
print('FIM DE JOGO')
          
"""