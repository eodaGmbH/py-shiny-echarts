from .option import ChartOption


class ExpressOption(object):
    series: list = list()
    kwargs: dict = dict()

    def to_option(self) -> ChartOption:
        kwargs = self.kwargs | {"series": self.series}
        return ChartOption(**kwargs)

    def to_dict(self) -> dict:
        return self.to_option().to_dict()


class Bar(ExpressOption):
    CHART_TYPE = "bar"

    def __init__(self, x: str, y: str, **kwargs) -> None:
        self.series = [{"name": y, "type": self.CHART_TYPE, "encode": {"x": x, "y": y}}]
        self.kwargs = kwargs


class Line(ExpressOption):
    pass


class Pie(ExpressOption):
    pass


class Scatter(ExpressOption):
    pass
