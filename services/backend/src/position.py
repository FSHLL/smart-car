class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def up(self):
        return Position(self.row - 1, self.col)

    def down(self):
        return Position(self.row + 1, self.col)

    def left(self):
        return Position(self.row, self.col - 1)

    def right(self):
        return Position(self.row, self.col + 1)

    def is_equal_to(self, position):
        return self.row == position.row and self.col == position.col

    def key(self):
        return f"({self.row}, {self.col})"