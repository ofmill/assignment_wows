from sources.paint.figure.Figure import FigureDefinition


class Canvas:
    _buffer: list
    _drawn_figures: list

    def __init__(self):
        self._buffer = list()
        self._drawn_figures = list()

    def get_buffer(self):
        return list(self._buffer)

    def get_drawn_figures(self):
        return list(self._drawn_figures)

    def add_figure(self, figure_definition: FigureDefinition):
        self._buffer.append(figure_definition)

    def draw_all(self):
        for definition in self._buffer:
            figure = definition.get_instance()
            figure.draw()
            self._drawn_figures.append(figure)
        self._buffer.clear()

    def erase_all(self):
        for figure in self._drawn_figures:
            figure.erase()
        self._drawn_figures.clear()
