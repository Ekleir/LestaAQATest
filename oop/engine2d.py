
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = 'black'

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.x}, {self.y}) with radius {self.radius} and color {self.color}'

    def draw(self):
        if self.color == 'black':
            print(f'Drawing Circle: ({self.x} {self.y}) with radius {self.radius}')
        else:
            print(f'Drawing Circle: ({self.x} {self.y}) with radius {self.radius}, color - {self.color}')


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.point1 = (x1, y1)
        self.point2 = (x2, y2)
        self.point3 = (x3, y3)
        self.color = 'black'

    def __repr__(self):
        return f'{self.__class__.__name__}: ({self.point1}, {self.point2}, {self.point3}) and color {self.color}'

    def draw(self):
        if self.color == 'black':
            print(f'Drawing Triangle: ({self.point1}, {self.point2}, {self.point3}')
        else:
            print(f'Drawing Triangle: ({self.point1}, {self.point2}, {self.point3}, color - {self.color}')


class Rectangle:
    def __init__(self, x1, y1, x2, x3):
        self.start_point = (x1, y1)
        self.width = x2
        self.height = x3
        self.color = 'black'

    def __repr__(self):
        return f'{self.__class__.__name__} from {self.start_point} sides: {self.width} x {self.height}' \
               f' and color {self.color}'

    def draw(self):
        if self.color == 'black':
            print(f'Drawing Rectangle: ({self.start_point} with width {self.width}, height {self.height}')
        else:
            print(f'Drawing Rectangle: ({self.start_point} with width {self.width}, height {self.height},'
                  f' color - {self.color}')


class Engine2D:
    canvas = []

    def __init__(self):
        self.color = 'black'

    def __str__(self):
        return f'Canvas with figures: {self.canvas}'

    def add_figures(self, *figures):
        for figure in figures:
            figure.color = self.color
            self.canvas.append(figure)

    def set_color(self, color):
        self.color = color

    def draw(self):
        for figure in self.canvas:
            figure.draw()
        self.canvas = []


if __name__ == '__main__':

    engine = Engine2D()

    print('***color - default - black***')
    triangle = Triangle(1, 1, 2, 3, 4, 5)
    circle = Circle(0, 0, 1)
    rectangle = Rectangle(0, 0, 1, 2)
    engine.add_figures(triangle, circle, rectangle)
    engine.add_figures(triangle)
    print(engine)

    print('\n***color - yellow***')
    engine.set_color('yellow')
    triangle_yellow = Triangle(11, 11, 21, 31, 41, 51)
    circle_yellow = Circle(10, 10, 11)
    rectangle_yellow = Rectangle(110, 110, 111, 112)
    engine.add_figures(triangle_yellow, circle_yellow, rectangle_yellow)
    print(engine)

    print('\n***color - white***')
    engine.set_color('white')
    circle_white = Circle(1210, 1210, 1211)
    engine.add_figures(circle_white)
    print(engine)

    print('\n***cleans***')
    engine.draw()
