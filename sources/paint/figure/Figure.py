from sources.paint.common.Color import Color


class Figure:
    def __init__(self) -> None:
        super().__init__()

    # in reality draw methods would've differed from each other in subclasses
    def draw(self):
        print("Drawing {}".format(self.__str__()))

    def erase(self):
        print("Erasing {}".format(self.__str__()))


class FigureDefinition:
    _color: Color

    def __init__(self):
        self._color = Color(0.0, 0.0, 0.0)

    def get_color(self):
        return self._color

    def set_color(self, color: Color):
        self._color = color

    def validate(self):
        pass

    def get_instance(self):
        pass
