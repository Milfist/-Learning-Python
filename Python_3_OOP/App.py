from models.Point import Point
from models.Rectangle import Rectangle


def main():
    point_a = Point(2, 3)
    point_b = Point(5, 5)
    rectangle = Rectangle(point_a, point_b)

    point_a.quadrant()
    point_b.quadrant()
    point_a.vector(point_b.axis_x, point_b.axis_y)
    point_b.vector(point_a.axis_x, point_a.axis_y)

if __name__ == "__main__":
    main()
