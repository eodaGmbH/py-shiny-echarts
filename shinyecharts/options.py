# DEPRECATED: Use 'express.Chart' instead

from __future__ import annotations

from dataclasses import dataclass, field

from pandas import DataFrame

from ._core import BaseDataClass, BaseOption, BaseOptionXY, df_to_pie_data


@dataclass
class ChartOption(BaseDataClass):
    """Chart option

    Note:
        See also [Option](https://echarts.apache.org/en/option.html).
    """

    title: dict = None
    legend: dict = None
    grid: dict = None
    x_axis: dict = field(default_factory=dict)
    y_axis: dict = field(default_factory=dict)
    polar: dict = None
    radius_axis: dict = None
    angle_axis: dict = None
    radar: dict = None
    data_zoom: list = None
    visual_map: list = None
    tooltip: dict = None
    # ...
    series: list = field(default_factory=list)


class Pie(BaseOption):
    """Pie Option"""

    CHART_TYPE = "pie"

    def __init__(
        self,
        series_options: dict = dict(),
        data: DataFrame | list = None,
        name: str = "name",
        value: str = "value",
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


class Line(BaseOptionXY):
    """Line Option"""

    CHART_TYPE = "line"


class Bar(BaseOptionXY):
    """Bar Option"""

    CHART_TYPE = "bar"


class Scatter(BaseOptionXY):
    """Scatter Option"""

    CHART_TYPE = "scatter"
