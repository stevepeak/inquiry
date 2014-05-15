from .helpers import *
from .garden import Garden
from .results import FigureResult


class Figure(object):
    __slots__ = ("id", "title", "help", "outline", "alias", "seed")

    def __init__(self, id, figure):
        self.id = id
        self.title = figure.pop('title') if 'title' in figure else None
        self.help = figure.pop('help') if 'help' in figure else None
        self.outline = figure.pop('outline')
        self.alias = array(figure.pop('alias')) if 'alias' in figure else []
        self.seed = figure

    def _process(self, navigator, paths, userkwargs, extra_data):
        # filter out empty paths and generate a garden
        garden = Garden(self, navigator, [p for p in paths if p], extra_data)
        # water down the garden with user arguments
        query, period = garden.harvest(navigator, userkwargs)
        # return a FigureResults
        return FigureResult(navigator, query, period, extra_data)
