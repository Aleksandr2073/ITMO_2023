class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rec1 = Rectangle(5, 10)
rec2 = Rectangle(8,5)
rec3 = Rectangle(11,11)
print(rec1.area(), rec1.perimeter())
print(rec2.area(), rec2.perimeter())
print(rec3.area(), rec3.perimeter())


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def subtraction(self):
        return self.a - self.b

m = Math(10, 2)
print(m.addition())
print(m.multiplication())
print(m.division())
print(m.subtraction())



class Button:

    def __init__(self, text, type, lok):
        self.text = text
        self.type = type
        self.lok = lok

    def click(self):
        return "Клик по кнопке - {}".format(self.text)

but1 = Button('Text Box', 'Кнопка', ' ')
but2 = Button('Check Box', 'Кнопка', ' ')
but3 = Button('Radio Button', 'Кнопка', ' ')
but4 = Button('Web Tables', 'Кнопка', ' ')
but5 = Button('Buttons', 'Кнопка', ' ')
but6 = Button('Links', 'Кнопка', ' ')
but7 = Button('Broken Links-Images', 'Кнопка', ' ')
but8 = Button('Upload and Download', 'Кнопка', ' ')
but9 = Button('Dynamic Properties', 'Кнопка', ' ')

print(but1.text)
print(but1.click())
print(but2.text)
print(but2.click())
print(but3.text)
print(but3.click())
print(but4.text)
print(but4.click())
print(but5.text)
print(but5.click())
print(but6.text)
print(but6.click())
print(but7.text)
print(but7.click())
print(but8.text)
print(but8.click())
print(but9.text)
print(but9.click())




