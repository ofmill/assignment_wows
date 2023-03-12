class Color:
    r: float
    g: float
    b: float

    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        return "[r: {}, g: {}, b: {}]".format(self.r, self.g, self.b)
