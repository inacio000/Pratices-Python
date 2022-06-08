class Ball:

    def __init__(self, color, circunference, material):
        self.color = color
        self.circunference = circunference
        self.material = material

    def change_color(self, new_color):
        self.color = new_color

    def show_color(self):
        print(self.color, self.circunference, self.material)


ball1 = Ball('Blue', 5.5, 'Saco')
ball1.show_color()

ball1.change_color('Red')
ball1.show_color()