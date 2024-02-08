from __future__ import annotations

from .option import ChartOption


# TODO: Make it private
class ExpressOption(object):
    """Base Express Option"""

    CHART_TYPE: str = "line"

    series: list = list()
    kwargs: dict = dict()

    def __init__(self, x: str = None, y: str = None, **kwargs) -> None:
        self.x = x
        self.series = [self._create_series(x, y)]
        self.kwargs = kwargs

    def _create_series(self, x: str, y: str) -> dict:
        return {"name": y, "type": self.CHART_TYPE, "encode": {"x": x, "y": y}}

    def add_series(self, y: str) -> ExpressOption:
        self.series.append(self._create_series(self.x, y))
        return self

    def to_option(self) -> ChartOption:
        kwargs = self.kwargs | {"series": self.series}
        return ChartOption(**kwargs)

    def to_dict(self) -> dict:
        return self.to_option().to_dict()


class Bar(ExpressOption):
    """Bar option"""

    CHART_TYPE = "bar"

    def __init__(self, x: str, y: str, **kwargs) -> None:
        super().__init__(x, y, **kwargs)
        self.kwargs = kwargs | {"x_axis": {"type": "category"}}


class Line(ExpressOption):
    """Line Option"""

    CHART_TYPE = "line"


class Scatter(ExpressOption):
    """Scatter Option"""

    CHART_TYPE = "scatter"


class Pie(ExpressOption):
    CHART_TYPE = "pie"

    def __init__(self, data, name: str, value: str, **kwargs):
        super().__init__(**kwargs | {"x_axis": None, "y_axis": None})
        self.series = [
            {
                "type": self.CHART_TYPE,
                "data": [
                    {"name": row[0], "value": row[1]}
                    for row in data[[name, value]].to_numpy()
                ],
            }
        ]
