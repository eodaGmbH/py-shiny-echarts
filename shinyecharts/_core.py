from __future__ import annotations

from dataclasses import asdict, dataclass

from pandas import DataFrame


# -------------------------
# Utils
# -------------------------
def snake_to_camel_case(snake_str: str) -> str:
    return snake_str[0].lower() + snake_str.title()[1:].replace("_", "")


def df_to_dataset(df: DataFrame = None) -> dict:
    return dict(dataset=dict(source=df.to_dict(orient="list")))
    # return {"dataset": {"source": [df.columns.to_list()] + df.to_numpy().tolist()}}


def df_to_pie_data(df: DataFrame, name: str, value: str) -> list:
    return [{"name": row[0], "value": row[1]} for row in df[[name, value]].to_numpy()]


@dataclass
class BaseDataClass(object):
    def to_dict(self):
        return asdict(
            self,
            dict_factory=lambda x: {
                snake_to_camel_case(k): v for (k, v) in x if v is not None
            },
        )


# -------------------------
# Option
# -------------------------
class BaseOption(object):
    CHART_TYPE: str = None

    option = dict()

    def to_dict(self) -> dict:
        return self.option


class BaseOptionXY(BaseOption):
    def _create_series(self, x: str, y: str, series_options: dict = None) -> dict:
        return {
            "name": y,
            "type": self.CHART_TYPE,
            "encode": {"x": x, "y": y},
        } | (series_options or dict())

    def __init__(
        self,
        x: str = None,
        y: str = None,
        series_options: dict = None,
        data: DataFrame = None,
        **kwargs,
    ) -> None:
        self.x = x
        x_axis = dict(type="category") if self.CHART_TYPE == "bar" else dict()
        series = [self._create_series(x, y, series_options)]
        defaults = dict(xAxis=x_axis, yAxis=dict())
        if isinstance(data, DataFrame):
            defaults.update(df_to_dataset(data))

        self.option = defaults | kwargs | {"series": series}

    def add_series(self, y: str, series_options: dict = None) -> BaseOptionXY:
        self.option["series"].append(self._create_series(self.x, y, series_options))
        return self
