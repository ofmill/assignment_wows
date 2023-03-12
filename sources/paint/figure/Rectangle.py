import sources.paint.helpers.CalculationsHelper as CalcHelper
import copy

from sources.paint.figure.Figure import Figure
from sources.paint.figure.Figure import FigureDefinition
from sources.paint.common.Coordinates import Coordinates
from sources.paint.figure.DefinitionValidationException import DefinitionValidationException


class RectangleDefinition(FigureDefinition):
    # point_a --- point_b
    #   |           |
    # point_c --- point_d
    point_a: Coordinates
    point_b: Coordinates
    point_c: Coordinates
    point_d: Coordinates

    def __init__(self, x0: int, y0: int, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
        super().__init__()
        self.point_a = Coordinates(x0, y0)
        self.point_b = Coordinates(x1, y1)
        self.point_c = Coordinates(x2, y2)
        self.point_d = Coordinates(x3, y3)

    def validate(self):
        if CalcHelper.compute_angle(self.point_a, self.point_b, self.point_c) != 90.0 or \
                CalcHelper.compute_angle(self.point_b, self.point_a, self.point_d) != 90.0 or \
                CalcHelper.compute_angle(self.point_c, self.point_a, self.point_d) != 90.0:
            raise DefinitionValidationException("All angles of the rectangle should be 90 degrees")

    def get_instance(self):
        return Rectangle(self)


class Rectangle(Figure):
    definition: RectangleDefinition

    def __init__(self, definition: RectangleDefinition) -> None:
        super().__init__()
        self.definition = copy.deepcopy(definition)

    def __str__(self) -> str:
        return "Rectangle: vertices {}, {}, {}, {}. Color: {}" \
            .format(self.definition.point_a.__str__(), self.definition.point_b.__str__(),
                    self.definition.point_c.__str__(), self.definition.point_d.__str__(),
                    self.definition.get_color())
