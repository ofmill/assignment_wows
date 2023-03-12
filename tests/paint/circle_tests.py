import pytest

from sources.paint.figure.Circle import CircleDefinition
from sources.paint.figure.DefinitionValidationException import DefinitionValidationException


def test_valid_definition():
    definition = CircleDefinition(0, 0, 1)
    definition.validate()


def test_zero_radius_is_not_allowed():
    definition = CircleDefinition(0, 0, 0)
    with pytest.raises(DefinitionValidationException):
        definition.validate()


def test_negative_radius_is_not_allowed():
    definition = CircleDefinition(0, 0, -1)
    with pytest.raises(DefinitionValidationException):
        definition.validate()