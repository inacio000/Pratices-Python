# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, 
# a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

from cabecalho import cabecalho


class Person:

    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def geting_old(self):
        if self.age < 21:
            self.height += 0.5
        self.age += 1

    def geting_fat(self, up_weight):
        self.weight += up_weight

    def losing_weight(self, dow_weight):
        self.weight -= dow_weight

    def to_grow(self, new_height):
        self.height += new_height

    def show_person(self):
        print(f'Name: {self.name}; \nAge: {self.age} years old; \nWeight: {self.weight}kg; \nHeight: {self.height}cm')


Inacio = Person('Inacio', 20, 48, 169)
Inacio.show_person()

cabecalho('GETING OLD')
Inacio.geting_old()
Inacio.show_person()

cabecalho('GETING FAT')
Inacio.geting_fat(2)
Inacio.show_person()

cabecalho('LOSING WEIGHT')
Inacio.losing_weight(1)
Inacio.show_person()
