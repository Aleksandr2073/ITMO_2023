class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return 'Автомобиль заведен'

    def stop(self):
        return 'Автомобиль заглушен'

    def years(self, year_new):
        self.years = year_new
        return self.years

    def types(self, type_new):
        self.types = type_new
        return self.types

    def colors(self, color_new):
        self.colors = color_new
        return self.colors

car = Car('White', 'Sedan', '2017')
print(car.start())
print(car.stop())
print(car.color, car.type, car.year)
print(car.years('2023'))
print(car.types('Bus'))
print(car.colors('Red'))



