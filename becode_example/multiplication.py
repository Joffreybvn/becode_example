
import numpy as np


class Multiplication:
    """
    Instantiate a multiplication operation.
    Multiply by the given multiplier.

    :param multiplier: Number used as multiplier.
    :type multiplier: int, float
    """

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        """
        Multiply a given number by a the multiplier.

        :param number: Number to multiply.
        :type number: int, float

        :return The result of the multiplication.
        :rtype: int, float
        """

        return np.dot(number, self.multiplier)
