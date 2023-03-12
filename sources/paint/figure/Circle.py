import copy

from sources.paint.figure.Figure import Figure
from sources.paint.figure.Figure import FigureDefinition
from sources.paint.common.Coordinates import Coordinates
from sources.paint.figure.DefinitionValidationException import DefinitionValidationException


class CircleDefinition(FigureDefinition):
    center: Coordinates
    radius: int

    def __init__(self, x: int, y: int, radius: int):
        super().__init__()
        self.center = Coordinates(x, y)
        self.radius = radius

    def validate(self):
        if not self.radius > 0:
            raise DefinitionValidationException("Radius should be greater than 0")

    def get_instance(self):
        return Circle(self)


class Circle(Figure):
    definition: CircleDefinition

    def __init__(self, definition: CircleDefinition) -> None:
        super().__init__()
        self.definition = copy.deepcopy(definition)

    def __str__(self) -> str:
        return "Circle: {} with radius {}. Color: {}."\
            .format(self.definition.center.__str__(), self.definition.radius, self.definition.get_color())
