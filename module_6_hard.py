import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        if not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in
                   (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int)
                                                         and side > 0 for side in
                                                         new_sides)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color)

        self.__radius = None
        if not isinstance(circumference, (int, float)) or circumference < 0:
            raise ValueError("Circumference must be a positive number.")

        self.radius = circumference / (2 * math.pi)
        self.set_sides(circumference)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()

        if not all(isinstance(side, (int, float)) and side > 0
            for side in (a, b, c)):
            raise ValueError("All sides must be positive numbers.")

        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge_length):
        super().__init__(color)

        if not isinstance(edge_length, (int, float)) or edge_length <=0:
            raise ValueError("Edge length must be a positive number.")

        self.set_sides(*[edge_length] * self.sides_count)

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3


# Пример использования классов
circle1 = Circle((200, 200, 100), 10)  # Создаем объект круга с цветом и длиной окружности
cube1 = Cube((222, 35, 130), 6)  # Создаем объект куба с цветом и длиной ребра

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменение цвета круга
print(circle1.get_color())  # Выводим текущий цвет круга: [55,66,77]
cube1.set_color(300, 70, 15)  # Попытка изменить цвет куба на некорректный
print(cube1.get_color())  # Выводим текущий цвет куба: [222,35,130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12)  # Попытка изменить стороны куба на некорректные
print(cube1.get_sides())  # Выводим текущие стороны куба: [6]*12
circle1.set_sides(15)  # Изменение стороны круга на новую длину окружности
print(circle1.get_sides())  # Выводим текущие стороны круга: [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Выводим длину окружности: ~15.71

# Проверка объёма (куба):
print(cube1.get_volume())  # Выводим объём куба: ~216