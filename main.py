
class Multiplication:
    """
    Instantiate a multiplication operation.
    Multiply by the given multiplier.

    :param multiplier: Number used as multiplier.
    :type multiplier: int
    """

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        """
        Multiply a given number by a the multiplier.

        :param number: Number to multiply.
        :type number: int

        :return The result of the multiplication.
        :rtype: int
        """

        return number * self.multiplier


# Instantiate a Multiplication object
multiplication = Multiplication(2)

# Call the multiply method
multiplication.multiply(5)
