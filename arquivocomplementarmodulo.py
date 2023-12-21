import random

pes_para_milhas = 5280
metros_para_km = 1000
beatles = ["John Lennon","Paul McCartney","George Harrison","Ringo Star"]

def obterextensao(filename):
    return filename[filename.index(".") + 1:]

def rodardados(num):
    return random.randint(1,num)