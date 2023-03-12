import pytest

from sources.paint.figure.Triangle import TriangleDefinition
from sources.paint.figure.DefinitionValidationException import DefinitionValidationException


def test_valid_triangle():
    definition = TriangleDefinition(-1, -1, 0, 1, 1, -1)
    definition.validate()


def test_all_points_on_same_line():
    definition = TriangleDefinition(-1, -1, 0, 0, 1, 1)
    with pytest.raises(DefinitionValidationException):
        definition.validate()