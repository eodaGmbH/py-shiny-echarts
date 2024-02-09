from __future__ import annotations

from ._core import BaseOption
from .options import ChartOption


# TODO: Make it private
# TODO: OBSOLETE
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
