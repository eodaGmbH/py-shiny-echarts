from __future__ import annotations

from echarts4py._core import BaseOption
from echarts4py.options import ChartOption

# "boundaryGap": False,
# "splitLine": {"show": True},
# "axisTick": {"interval": 0.5},
# "minorTick": {},


class Line(BaseOption):
    """Line Option"""

    CHART_TYPE = "line"

    def __init__(self, x: str, y: str, data=None, **kwargs) -> None:
        self.data = data
        series = [{"name": y, "data": data[y].to_list(), "type": self.CHART_TYPE}]
        self.option = kwargs | {
            "x_axis": {
                "data": data[x].to_list(),
                "type": "category",
            },
            "series": series,
        }

    def add(self, y: str) -> Line_:
        self.option["series"].append(
            {"name": y, "data": self.data[y].to_list(), "type": self.CHART_TYPE}
        )
        return self

    def to_dict(self) -> dict:
        return ChartOption(**self.option).to_dict()
