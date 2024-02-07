from dataclasses import dataclass, field

from ._core import BaseDataClass


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
