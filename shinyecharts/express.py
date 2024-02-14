from __future__ import annotations

from pandas import DataFrame

from .chart import Chart as BaseChart
from .chart import InitOptions


class Chart(BaseChart):
    def __init__(self, options: InitOptions = InitOptions()):
        super().__init__(options)
        self._option = dict(xAxis=dict(), yAxis=dict())
        self.legend()

    def _update_option(self, **kwargs):
        self._option.update(**kwargs)

    def dark(self) -> Chart:
        self._theme = "dark"
        return self

    def data(self, df: DataFrame) -> Chart:
        self._data = df
        return self

    def x_axis(self, type: str = "value") -> Chart:
        self._update_option(xAxis=dict(type=type))
        return self

    def y_axis(self):
        return self

    def encode(
        self, x: str | int = "x", y: str | int = "y", type: str = "line", **kwargs
    ) -> Chart:
        if type == "bar":
            self.x_axis("category")

        series = dict(name=y, type=type, encode=dict(x=x, y=y)) | kwargs
        if "series" in self._option.keys():
            self._option["series"].append(series)
        else:
            self._update_option(series=[series])
        return self

    def legend(self, show=True, **kwargs) -> Chart:
        self._option.update(legend=dict(show=True) | kwargs)
        return self


# -------------------------
class PieChart(object):
    pass


class BarChart(object):
    pass


class LineChart(object):
    pass


class ScatterChart(object):
    pass
