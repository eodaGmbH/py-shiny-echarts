from __future__ import annotations

from pandas import DataFrame

from ._enums import SeriesType
from .chart import Chart as BaseChart
from .chart import InitOptions


class Chart(BaseChart):
    _series_type: str = "line"

    def __init__(self, options: InitOptions = InitOptions()):
        super().__init__(None, options)
        self._option = dict(xAxis=dict(), yAxis=dict())
        self.legend()

    # TODO: Use 'attr' from base Chart
    def _update_option(self, **kwargs) -> None:
        self._option.update(**kwargs)

    def _add_series(self, series: dict) -> None:
        if "series" in self._option.keys():
            self._option["series"].append(series)
        else:
            self._update_option(series=[series])

    def dark(self) -> Chart:
        self._theme = "dark"
        return self

    def data(self, df: DataFrame) -> Chart:
        self._data = df
        return self

    def series_type(self, series_type: SeriesType | str) -> Chart:
        self._series_type = SeriesType(series_type).value
        return self

    def x_axis(self, type: str = "value", **kwargs) -> Chart:
        self._update_option(xAxis=dict(type=type) | kwargs)
        return self

    def y_axis(self):
        return self

    # TODO: Rename to series_options!? But which method will then add the series?
    def series(self, type: SeriesType | str, **kwargs) -> Chart:
        type = SeriesType(type).value
        if type == "bar":
            self.x_axis("category")

        if type == "pie":
            self._update_option(xAxis=None, yAxis=None)

        self._add_series(dict(type=type) | kwargs)
        return self

    def encode(
        self,
        x: str | int = "x",
        y: str | int = "y",
        type: SeriesType | str = None,
        **kwargs,
    ) -> Chart:
        type = type or self._series_type
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

    def tooltip(self, show: bool = True, trigger: str = "item", **kwargs) -> Chart:
        self._option.update(tooltip=dict(show=show, trigger=trigger) | kwargs)
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
