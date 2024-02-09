from htmltools import Tag
from shiny.render.renderer import Jsonifiable, Renderer

from .chart import Chart
from .ui import output_chart


class ChartRenderer(Renderer[Chart]):
    """A decorator for a function that returns a chart"""

    def auto_output_ui(self) -> Tag:
        return output_chart(self.output_id)

    async def transform(self, value: Chart) -> Jsonifiable:
        return value.to_dict()
