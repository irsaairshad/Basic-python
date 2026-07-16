class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_point_on_line(self, point_obj):
        result = self.a * point_obj.x + self.b * point_obj.y + self.c
        return result == 0


if __name__ == "__main__":
    line = Line(1, 1, -2)
    pt = Point(1, 1)
    print(line.is_point_on_line(pt))
