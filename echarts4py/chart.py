from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

from pandas import DataFrame

from .express import ExpressOption
from .option import ChartOption


@dataclass
class InitOptions(object):
    width: int = 600
    height: int = 400
    renderer: Literal["svg", "canvas"] = "svg"


class Chart(object):
    """Chart"""

    def __init__(
        self,
        init_options: InitOptions = InitOptions(),
        theme: str | None = "dark",
        data: DataFrame = None,
    ) -> None:
        self.init_options = init_options
        self.theme = theme
        self.data = data
        self.option = {}

    def set_option(self, option: dict | ChartOption | ExpressOption) -> Chart:
        self.option = option if isinstance(option, dict) else option.to_dict()
        return self

    def to_dict(self) -> dict:
        dataset = (
            {
                "dataset": {
                    "source": [self.data.columns.to_list()]
                    + self.data.to_numpy().tolist()
                }
            }
            if isinstance(self.data, DataFrame)
            else {}
        )
        return {
            "initOptions": asdict(self.init_options),
            "option": dataset | self.option,
            "theme": self.theme,
        }
