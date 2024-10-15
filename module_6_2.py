class Vehicle:
    """Класс транспорта"""

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner #владелец транспорта
        self.__model = model #модель (марка) транспорта
        self.__engine_power = engine_power #мощность двигателя
        self.__color = color #название цвета

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self): #название модели
        return f'Модель: {self.__model}'

    def get_horsepower(self): #Мощность двигателя
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self): #цвет транспорта
        return f'Цвет: {self.__color}'

    def print_info(self): #распечатывает результаты
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    """Класс седана. Наследник класса транспорта"""
    __PASSENGERS_LIMIT = 5 #в седан может поместиться только 5 пассажиров


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
