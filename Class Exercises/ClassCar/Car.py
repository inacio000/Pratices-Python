class Car:

    def __init__(self, gasoline_consumtion):
        self.gasoline_consumtion = gasoline_consumtion
        self.gasoline_in_the_tank = 0

    def running(self, distance):
        gasoline_suppled = distance / self.gasoline_consumtion
        self.gasoline_in_the_tank -= gasoline_suppled
        return gasoline_suppled

    def get_gasoline_level(self):
        return f'{self.gasoline_in_the_tank:.2f}'

    def supply_gasoline(self, liter_quantity):
        self.gasoline_in_the_tank += liter_quantity


mercedes = Car(15)
mercedes.supply_gasoline(20)
mercedes.running(100)
print(mercedes.get_gasoline_level())
