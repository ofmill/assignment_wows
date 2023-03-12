import sources.paint.helpers.CalculationsHelper as CalcHelper
import copy

from sources.paint.figure.DefinitionValidationException import DefinitionValidationException
from sources.paint.figure.Figure import Figure
from sources.paint.figure.Figure import FigureDefinition
from sources.paint.common.Coordinates import Coordinates


class TriangleDefinition(FigureDefinition):
    point_a: Coordinates
    point_b: Coordinates
    point_c: Coordinates

    def __init__(self, x0: int, y0: int, x1: int, y1: int, x2: int, y2: int):
        super().__init__()
        self.point_a = Coordinates(x0, y0)
        self.point_b = Coordinates(x1, y1)
        self.point_c = Coordinates(x2, y2)

    def validate(self):
        length_a_b = CalcHelper.two_points_length(self.point_a, self.point_b)
        length_a_c = CalcHelper.two_points_length(self.point_a, self.point_c)
        length_b_c = CalcHelper.two_points_length(self.point_b, self.point_c)

        if not length_a_b < length_a_c + length_b_c:
            raise DefinitionValidationException("AB side is no less than the sum of AC and BC")
        if not length_a_c < length_a_b + length_b_c:
            raise DefinitionValidationException("AC side is no less than the sum of AB and BC")
        if not length_b_c < length_a_c + length_a_b:
            raise DefinitionValidationException("BC side is no less than the sum of AC and AB")

    def get_instance(self):
        return Triangle(self)


class Triangle(Figure):
    definition: TriangleDefinition

    def __init__(self, definition: TriangleDefinition) -> None:
        super().__init__()
        self.definition = copy.deepcopy(definition)

    def __str__(self) -> str:
        return "Triangle: vertices {}, {}, {}. Color: {}."\
            .format(self.definition.point_a.__str__(), self.definition.point_b.__str__(),
                    self.definition.point_c.__str__(), self.definition.get_color())
