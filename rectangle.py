from shape import Shape

class Rectangle(Shape):

    def __init__(self, a, b):
        """
        Constructs a Rectangle object.

        :param length: float -> length of the rectangle
        :param width: float -> width of the rectangle
        """
        self.check_if_args_not_below_zero(a, b)
        self.a = a
        self.b = b

    def get_area(self):
        """
        Calculates the area of the rectangle using the formula: length * width

        :return: float -> area of the rectangle
        """
        area = self.a * self.b
        return area

    def get_perimeter(self):
        """
        Calculates the perimeter of the rectangle using the formula: 2 * (length + width)

        :return: float -> perimeter of the rectangle
        """
        perimeter =  2 * (self.a + self.b)
        return perimeter

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        :return: string
        """
        return f"Rectangle, a={self.a:0.2f}, b={self.b:0.2f}"

    @classmethod
    def get_area_formula(cls):
        """
        Returns the formula for calculating the area of a rectangle.

        :return: string
        """
        return "a * b"

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns the formura for calcualting the perimeter of a rectangle.

        :return: string
        """
        return "2(a + b)"
