from __future__ import annotations

from .option import ChartOption


class ExpressOption(object):
    CHART_TYPE: str = "line"

    series: list = list()
    kwargs: dict = dict()

    def __init__(self, x: str, y: str, **kwargs) -> None:
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
    CHART_TYPE = "bar"

    def __init__(self, x: str, y: str, **kwargs) -> None:
        super().__init__(x, y, **kwargs)
        self.kwargs = kwargs | {"x_axis": {"type": "category"}}


class Line(ExpressOption):
    pass


class Pie(ExpressOption):
    pass


class Scatter(ExpressOption):
    pass
