import arcade

class Figure:
    def __init__(self, color, *sides):
        self.sides_count = 0
        self.__color = list(color)
        self.sides = []
        self.filled = True
        self.set_sides(*sides)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.sides

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color, circumference):
        super().__init__(color, 1)  # У круга одна сторона
        self.__radius = circumference / (2 * 3.14159265)  # Длина окружности = 2 * π * r
        self.sides = [1]  # Одно измерение

    def get_square(self):
        return 3.14159265 * (self.__radius ** 2)


class Triangle(Figure):
    def __init__(self, color, a, b, c):
        super().__init__(color, 3)  # У треугольника 3 стороны
        self.set_sides(a, b, c)

    def get_square(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    def __init__(self, color, side):
        super().__init__(color, 12)  # У куба 12 рёбер
        self.sides = [side] * 12  # 12 одинаковых сторон

    def get_volume(self):
        return self.sides[0] ** 3  # Объём куба: a^3


# Пример использования
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # Вывод: [55, 66, 77]
