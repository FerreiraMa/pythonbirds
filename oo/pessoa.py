class Pessoa:
    olhos = 2 #Atributo de classe ou default (Usado quando o valor é comum para todos objetos.
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

    #Atributo dinâmico (Não é uma boa prática)
    marcelo.sobrenome = 'Santos'
    print(marcelo.sobrenome)
    print(ferreira.__dict__) #Conferir atributos de instâncias do objeto
    print(marcelo.__dict__)
    del marcelo.filhos #Remove o atributo dinamicamente

    #Atributo default ou atributo de classe
    print(Pessoa.olhos)
    print(marcelo.olhos)
    print(id(Pessoa.olhos),id(ferreira.olhos), id(marcelo.olhos))





