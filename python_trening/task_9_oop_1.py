from task_9_checks import Checks

class Input(Checks):

    def __init__(self,text, lok):
        super().__init__(lok)
        self.text = text
        self.lok = lok

    def click(self):
        return "Клик по кнопке - {}".format(self.lok)

search = Input('Вход', 'Вход')

print(search.text, search.click())


class Button(Checks):

    def __init__(self, text, lok):
        super().__init__(lok)
        self.text = text
        self.lok = lok

start = Button('Пуск','внизу слева')
print(start.text, start.lok)


class Title(Checks):

    def __init__(self, text, lok):
        super().__init__(lok)
        self.text = text
        self.lok = lok

header = Title('Заголовок', 'вверху страницы')
print(header.text, header.lok)


class Link(Checks):

    def __init__(self, text, lok):
        super().__init__(lok)
        self.text = text
        self.lok = lok

    def click(self):
        return "Клик по ссылке - {}".format(self.lok)

home = Link('Домашняя страница ', '/home')

print('Переход на ' + home.text + home.click())

