import pytest

from sources.paint.figure.Rectangle import RectangleDefinition
from sources.paint.figure.DefinitionValidationException import DefinitionValidationException


def test_valid_definition():
    definition = RectangleDefinition(-1, 1, 1, 1, -1, -1, 1, -1)
    definition.validate()

def test_if_not_all_agles_are_90_degrees():
    definition = RectangleDefinition(-1, 1, 1, 1, -1, -1, 1, -2)
    with pytest.raises(DefinitionValidationException):
        definition.validate()
