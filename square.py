"""
Implement this class.
Recall that every square is a rectangle.
Therefore the Square class should inherit from the Rectangle class.
Do NOT implement the get_area() and get_perimeter() methods here.
Those methods should be inherited from the parent class.
"""
from rectangle import Rectangle

class Square(Rectangle):
    """
    A class representing a square, which is a special case of rectangle where all sides are equal.
    Inherits from the Rectangle class.
    """

    def __init__(self, a):
        """
        Initializes a Square object with the given side length.

        :Args: float -> The length of each side of the square.
        """
        super().__init__(a, a)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        :returns: string 
        """
        return f"Square, a={self.a:0.2f}"

    @classmethod
    def get_area_formula(cls):
        """
        Returns the formula for calculating the area of a square.

        :returns: string 
        """
        return "a^2"

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns the formula for calcualting the perimeter of a square.

        :returns: string 
        """
        return "4 * a"
