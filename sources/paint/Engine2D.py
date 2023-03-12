import copy

from sources.paint.Canvas import Canvas
from sources.paint.figure.Figure import FigureDefinition
from sources.paint.common.Color import Color


class Engine2D:
    _canvas: Canvas
    _current_color: Color

    def __init__(self):
        self._canvas = Canvas()
        self._current_color = Color(0.0, 0.0, 0.0)

    def get_canvas(self):
        return self._canvas

    def set_color(self, color: Color):
        self._current_color = color

    def get_color(self):
        return self._current_color

    def add_figure(self, figure_definition: FigureDefinition):
        figure_definition.validate()
        definition = copy.deepcopy(figure_definition)
        definition.set_color(self._current_color)
        self._canvas.add_figure(definition)

    def draw(self):
        self._canvas.draw_all()
        self._canvas.erase_all()
