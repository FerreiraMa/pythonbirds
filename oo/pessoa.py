class Pessoa:
    olhos = 2 #Atributo de classe ou default (Usado quando o valor é comum para todos objetos.
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}, sei ID é {id(self)}'

    #Método de Classes
    @staticmethod
    def metodo_estatico(): #Independe do objeto, por este motivo não recebe 'self'
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls): #Utilizar quando queremos acessar atributos da própria classe
        return f'{cls} - olhos {cls.olhos}'

    #Herança
class Homem(Pessoa): #A classe homem herda da classe Pai Pessoa
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai} Aperto de Mão'

class Mutante(Pessoa):
    olhos =  3 #Sobrescrita de Atributo

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

    #executando o método
    print(Pessoa.metodo_estatico()) #Direto da classe
    print(marcelo.metodo_estatico()) #Através do objeto
    print(Pessoa.nome_e_atributos_de_classes())
    print(marcelo.nome_e_atributos_de_classes())

    #Sobrescrita de atributo de classe
    ferreira = Mutante(nome='Ferreira') #Sobrescrita de atributo
    print(ferreira.olhos)

    #Sobrescrita de Método
    ferreira = Homem(nome='Ferreira')
    print(ferreira.cumprimentar())
    print(marcelo.cumprimentar())





