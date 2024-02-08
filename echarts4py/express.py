from __future__ import annotations

from pandas import DataFrame

from ._core import BaseOption, df_to_dataset, df_to_pie_data
from .option import ChartOption


# TODO: Make it private
class ExpressOption(BaseOption):
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
    """Bar Option"""

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


class Pie(BaseOption):
    """Pie Option"""

    CHART_TYPE = "pie"

    def __init__(
        self,
        data: DataFrame | list,
        name: str = "name",
        value: str = "value",
        series_options: dict = dict(),
        **kwargs,
    ) -> None:
        if isinstance(data, DataFrame):
            data = df_to_pie_data(data, name, value)

        self.series = [series_options | {"type": self.CHART_TYPE, "data": data}]
        self.option = (
            kwargs | {"x_axis": None, "y_axis": None} | {"series": self.series}
        )

    def to_dict(self) -> dict:
        return ChartOption(**self.option).to_dict()
