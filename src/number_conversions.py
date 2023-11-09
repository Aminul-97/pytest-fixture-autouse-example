class NumberConversions:
    """
    Class converts decimal number to Binary, Octal and Hexadecimal
    """

    def __init__(self, num: int) -> None:
        self.num = num

    def convert_to_binary(self):
        """
        Converts Decimal to Binary
        """
        return bin(self.num)

    def convert_to_octal(self):
        """
        Converts Decimal to Octal
        """
        return oct(self.num)

    def convert_to_hexadecimal(self):
        """
        Converts Decimal to Hexadecimal
        """
        return hex(self.num)
