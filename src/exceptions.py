
class OutOfBoundsError(Exception):
    """raised when user chooses column not in range(0, M)"""

    def __init__(self):
        self.message = "Out of Bounds!"

    def __str__(self):
        return repr(self.message)


class ColumnFullError(Exception):
    """raised when user chooses column that is full"""

    def __init__(self):
        self.message = "Column is Full!"

    def __str__(self):
        return repr(self.message)

