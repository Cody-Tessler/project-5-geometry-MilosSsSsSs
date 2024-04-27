from shape import Shape
import math

class Circle(Shape):

    def __init__(self, r):
        """
        Constructs a Circle object.

        :param r: float -> radius of the circle
        """
        self.check_if_args_not_below_zero(r)
        self.r = r
    
    def get_area(self):
       """
       Calculates the area of the circle using the formula: pi * r^2

       :return: float -> area of the circle
       """
       return math.pi*(self.r**2)
        

    def get_perimeter(self):
        """
        Calculates the perimeter (circumference) of the circle using the formula: 2 * pi * r

        :return: float -> perimeter of the circle
        """
        return 2*math.pi*self.r 

    def __str__(self):
        """
        Returns a string representation of the Circle object.

        :return: string
        """
        return f"Circle, r={self.r:0.2f}"

    @classmethod
    def get_area_formula(cls):
        """
        Returns the formula for calculating the area of a circle.

        :return: string
        """
        return "pi*r^2"

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns the formula for calculating the perimeter of a circle.

        :return: string
        """
        return "pi*r*2"

