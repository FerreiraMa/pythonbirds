class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__== '__main__':
    #p = Pessoa('Marcelo')
    #print(Pessoa.cumprimentar(p))
    #print(id(p))
    #print(p.cumprimentar())
    #p.nome = 'Marcelo'
    #print(p.nome)
    #p.nome = 'Ferreira'
    #print(p.idade)

    #Atributo complexo
    ferreira = Pessoa(nome='Ferreira')   #filho de Marcelo, atribuido no objeto marcelo
    marcelo = Pessoa(ferreira, nome='Marcelo')
    print(Pessoa.cumprimentar(marcelo))
    print(id(marcelo))
    print(marcelo.cumprimentar())
    print(marcelo.nome)
    print(marcelo.idade)
    for filho in marcelo.filhos:
        print(filho.nome)





