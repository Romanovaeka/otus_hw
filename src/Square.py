import random


class Figure:

    def __init__(self, name):
        self.name = name

    FIGURE_AREA = [
        "Circle": c.area(),
        "Rectangle": r.area,
        "Square": s.area(),
        "Tiangle": t.area()
    ]
    @property
    def get_figure_area(self):
        return random.choice(FIGURE_AREA)

    @property
    def check_name(self, name):
        if name  in [Circle, Rectangle, Square, Ttiangle]:
            self.check_name = True
        else: print(f"raise ValueError")


class Square(Figure):

    def __int__(self, a):
        Figure.__init__(self)
        self.a = a


    @property
    def area(self, a):
        area = self.a ** 2
        area(5)
        return area


    @property
    def perimeter(self, a):
        perimetr = self.a * 4
        perimetr(5)
        return perimetr



    @property
    def add_area(self):
        f.check_name = True
        sum = s.area + f.get_figure_area
        return sum
