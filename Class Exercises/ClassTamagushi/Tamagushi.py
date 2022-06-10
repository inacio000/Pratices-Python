class BichoVirtual:

    def __init__(self, name, age, hungry=100, health=100):
        self.name = name
        self.age = age
        self.hungry = hungry
        self.health = health

    def humor(self):
        if self.hungry >= 70 and self.health >= 70:
            return '\033[32mI\'m happy\033[m'

        elif self.hungry >= 50 and self.health >= 50:
            return '\033[33mI\'m not so good\033[m'

        elif self.hungry >= 30 and self.health >= 30:
            return '\033[31mI\'m very hungry\033[m'

        else:
            return '\033[31mI\'m so weak!\033[m'

    def mood(self):
        print(self.humor())


bicho1 = BichoVirtual('Kaba', 1, 20, 50)
bicho1.mood()
