from unittest.mock import call
from sources.paint.Engine2D import Engine2D
from sources.paint.common.Color import Color
from sources.paint.figure.Circle import CircleDefinition
from sources.paint.figure.Circle import Circle
from sources.paint.figure.Triangle import TriangleDefinition
from sources.paint.figure.Triangle import Triangle
from sources.paint.figure.Rectangle import RectangleDefinition
from sources.paint.figure.Rectangle import Rectangle


def test_figure_definition_is_validated_during_addition(mocker):
    engine = Engine2D()
    circle_definition = CircleDefinition(0, 1, 2)
    validation_spy = mocker.spy(circle_definition, "validate")

    engine.add_figure(circle_definition)

    assert validation_spy.call_count == 1


def test_add_figure_through_engine_adds_it_to_canvas():
    engine = Engine2D()
    canvas = engine.get_canvas()
    circle = CircleDefinition(0, 0, 1)

    engine.add_figure(circle)

    assert len(canvas.get_buffer()) == 1


def test_adding_definition_does_not_cause_drawing(mocker):
    engine = Engine2D()
    canvas = engine.get_canvas()
    circle = CircleDefinition(0, 0, 1)
    instantiation_spy = mocker.spy(circle, 'get_instance')

    engine.add_figure(circle)

    assert instantiation_spy.call_count == 0
    assert len(canvas.get_drawn_figures()) == 0


def test_able_to_change_engine_color():
    engine = Engine2D()

    color_1 = Color(1.0, 1.0, 1.0)
    engine.set_color(color_1)
    assert engine.get_color().__eq__(color_1)

    color_2 = Color(0.5, 0.5, 0.5)
    engine.set_color(color_2)
    assert engine.get_color().__eq__(color_2)


def test_changing_engine_color_affects_new_figures():
    engine = Engine2D()
    color_1 = Color(1.0, 1.0, 1.0)
    engine.set_color(color_1)
    circle_1 = CircleDefinition(0, 0, 1)

    engine.add_figure(circle_1)

    assert engine.get_canvas().get_buffer()[0].get_color().__eq__(color_1)


def test_changing_engine_color_does_not_affect_already_added_figures():
    engine = Engine2D()
    color_1 = Color(1.0, 1.0, 1.0)
    engine.set_color(color_1)
    circle_1 = CircleDefinition(0, 0, 1)
    engine.add_figure(circle_1)

    color_2 = Color(0.5, 0.5, 0.5)
    engine.set_color(color_2)

    assert engine.get_canvas().get_buffer()[0].get_color().__eq__(color_1)


def test_engine_draw_function_erases_only_after_drawing(mocker):
    engine = Engine2D()
    circle_definition = CircleDefinition(0, 0, 1)
    circle = mocker.Mock(spec=Circle)
    mocker.patch('sources.paint.figure.Circle.CircleDefinition.get_instance', return_value=circle)
    triangle_definition = TriangleDefinition(-1, 0, 0, 1, 1, 0)
    triangle = mocker.Mock(spec=Triangle)
    mocker.patch('sources.paint.figure.Triangle.TriangleDefinition.get_instance', return_value=triangle)
    rectangle_definition = RectangleDefinition(-1, 1, 1, 1, -1, -1, 1, -1)
    rectangle = mocker.Mock(spec=Rectangle)
    mocker.patch('sources.paint.figure.Rectangle.RectangleDefinition.get_instance', return_value=rectangle)
    engine.add_figure(circle_definition)
    engine.add_figure(triangle_definition)
    engine.add_figure(rectangle_definition)

    engine.draw()

    assert circle.mock_calls == [call.draw(), call.erase()]
    assert triangle.mock_calls == [call.draw(), call.erase()]
    assert rectangle.mock_calls == [call.draw(), call.erase()]


def test_engine_draw_function_draws_all_and_erases_all(mocker):
    engine = Engine2D()
    circle_definition_1 = CircleDefinition(0, 0, 1)
    circle_definition_2 = CircleDefinition(1, 1, 2)
    circle_definition_3 = CircleDefinition(2, 2, 3)
    circle = mocker.Mock(spec=Circle)
    mocker.patch('sources.paint.figure.Circle.CircleDefinition.get_instance', return_value=circle)
    engine.add_figure(circle_definition_1)
    engine.add_figure(circle_definition_2)
    engine.add_figure(circle_definition_3)

    engine.draw()

    assert circle.mock_calls == [call.draw(), call.draw(), call.draw(), call.erase(), call.erase(), call.erase()]
