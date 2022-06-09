class Monkey:

    def __init__(self, name: str):
        self.name = name
        self.stomach = []

    def eat(self, food):
        self.stomach.append(food)

    def see_stomach(self):
        if len(self.stomach) <= 0:
            print('\033[31mEmpty stomach\033[m')
        else:
            print(f'Stomach: {self.stomach}')

    def digest_stomach(self):
        if len(self.stomach) > 0:
            self.stomach.pop(0)
        else:
            print('I can\'t digest, my stomach is empty')
