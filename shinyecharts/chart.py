from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Literal

from pandas import DataFrame

from ._core import BaseOption, df_to_dataset
from .options import ChartOption


@dataclass
class InitOptions(object):
    width: int = 600
    height: int = 400
    renderer: Literal["svg", "canvas"] = "svg"


# TODO: Move to _core
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

        # TODO: Move to class attributes
        self.option = dict()

    # TODO: Remove
    def set_pie_data(self, data: DataFrame) -> Chart:
        pass

    # Set option attributes
    def attr(self, **kwargs) -> Chart:
        pass

    # TODO: Set data here
    def set_data(self, data: DataFrame) -> Chart:
        pass

    def set_option(self, option: dict | ChartOption | BaseOption) -> Chart:
        self.option = option if isinstance(option, dict) else option.to_dict()
        return self

    def to_dict(self) -> dict:
        dataset = (
            df_to_dataset(self.data) if isinstance(self.data, DataFrame) else dict()
        )
        return {
            "initOptions": asdict(self.init_options),
            "option": dataset | self.option,
            "theme": self.theme,
        }
