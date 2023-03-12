class Coordinates:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)
