from shape import Shape
import math

class Pentagon(Shape):

    def __init__(self, a):
        """
        Constructs a Pentagon object.

        :param r: float -> length of a side of the pentagon
        """
        self.check_if_args_not_below_zero(a)
        self.a = a

    def get_area(self):
        """
       Calculates the area of the pentagon using the formula: (1/4) * sqrt(5 * (5 + 2 * sqrt(5))) * a^2

       :return: float -> area of the pent
       """
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.a**2

    def get_perimeter(self):
        """
        Calculates the perimeter of the pentagon by multiplying the length of a side by 5.

        :return: float -> perimeter of the pentagon
        """
        return 5 * self.a

    def __str__(self):
        """
        Returns a string representation of the Pentagon object.

        :return: string
        """
        return f"Pentagon, a={self.a:0.2f}"

    @classmethod
    def get_area_formula(cls):
        """
        Returns the formula for calculating the area of a pentagon.

        :return: string
        """
        return "(1/4) * sqrt(5 * (5 + 2 * sqrt(5))) * a^2"

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns the formula for calculating the perimeter of a pentagon.

        :return: string
        """
        return "5 * a"
