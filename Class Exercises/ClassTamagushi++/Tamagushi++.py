from random import randint
from cabecalho import cabecalho


class VirtualAnimal:

    def __init__(self, name, age, health, hungry):
        self.name = name
        self.age = age
        self.health = health
        self.hungry = hungry

    def humor(self):
        return f'{self.hungry * self.health:.2f}'

    def feed_the_animal(self, quantity_food):
        if 0 <= quantity_food <= 100:
            self.hungry -= self.hungry * (quantity_food / 100)

    def playing(self, how_long):
        if 0 <= how_long <= 100:
            self.hungry += self.health * (how_long / 100)

#     SECOND STEP
    def str(self):
        print(f'Name: {self.name} \nAge: {self.age} \nHealth: {self.health} \nHungry: {self.hungry}')


cabecalho('TESTING THE FIRST STEP')
animal1 = VirtualAnimal('TAMAGUSHI', 3, 6, 3)
animal1.humor()
animal1.feed_the_animal(50)
animal1.humor()
animal1.playing(20)
animal1.humor()

cabecalho('TESTING THE SECOND STEP')
animal1.str()
print()

cabecalho('TESTING THE THIRD STEP')
print()
animal2 = VirtualAnimal('Cat', 4, randint(0, 10), randint(0, 10))
animal3 = VirtualAnimal('Donkey', 5, randint(0, 10), randint(0, 10))
animal4 = VirtualAnimal('Dog', 4, randint(0, 10), randint(0, 10))
farm = list()
farm.append(animal2)
farm.append(animal3)
farm.append(animal4)

opc = 0
while opc != 4:
    cabecalho('FARM')
    print('[1] Feed all the animals \n[2] Play with all the animals '
          '\n[3] Listen to all the animals \n[4] Exit')
    opc = int(input('Options: '))

    if opc == 1:
        food = int(input('Feed all the animals with: '))
        for c in range(3):
            farm[c].feed_the_animal(food)

    elif opc == 2:
        how_long_time = int(input('How long time will you play with all the animals? '))
        for c in range(3):
            farm[c].playing(how_long_time)

    elif opc == 3:
        for c in range(3):
            print(f'{farm[c].name}: {farm[c].humor()}')

    elif opc == 4:
        break

    else:
        print('\033[31mInvalid option! \nTry again...\033[m')
