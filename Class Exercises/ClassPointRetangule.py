class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Retangule:

    def __init__(self, width, height):
        self.width = width
        self.heigth = height

    def find_center(self):
        center_x = (self.width.x + self.heigth.x) / 2.0
        center_y = (self.width.y + self.heigth.y) / 2.0
        return f'\nX = {center_x} \nY= {center_y}'


x1 = float(input('Enter the x coordinate of the lower left corner: '))
y1 = float(input('Enter the y coordinate of the lower left corner: '))
Corner1 = Point(x1, y1)

x2 = float(input('Enter the x coordinate of the upper right corner: '))
y2 = float(input('Enter the y coordinate of the upper right corner: '))
Corner2 = Point(x2, y2)

retangule = Retangule(Corner1, Corner2)
print(f'Central Point: {retangule.find_center()}')
