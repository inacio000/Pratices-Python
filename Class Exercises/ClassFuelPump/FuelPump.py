class FuelPump:

    def __init__(self, fuel_type: str, value_per_liter, fuel_quantity):
        self.fuel_type = fuel_type
        self.value_per_liter = value_per_liter
        self.fuel_quantity = fuel_quantity

    def supply_by_value(self, value):
        liter_quantity_suppled = value / self.value_per_liter
        self.change_fuel_quantity(self.fuel_quantity - liter_quantity_suppled)
        return liter_quantity_suppled

    def supply_per_liter(self, liter_quantity):
        amount_to_be_paid = liter_quantity * self.value_per_liter
        self.change_fuel_quantity(self.fuel_quantity - liter_quantity)
        return amount_to_be_paid

    def change_value(self, new_value_per_liter):
        self.value_per_liter = new_value_per_liter

    def change_fuel(self, new_fuel_type):
        self.fuel_type = new_fuel_type

    def change_fuel_quantity(self, new_fuel_quantity):
        self.fuel_quantity = new_fuel_quantity


vehicle = FuelPump('Gasoline', 5, 500)

vehicle.supply_by_value(150)
print(vehicle.fuel_quantity)

vehicle.supply_per_liter(30)
print(vehicle.fuel_quantity)
