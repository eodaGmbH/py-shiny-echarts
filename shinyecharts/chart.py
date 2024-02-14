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

    _theme: str = None
    _option: dict = dict()
    _data: DataFrame = None

    def __init__(
        self,
        init_options: InitOptions = InitOptions(),
        theme: str = None,
        data: DataFrame = None,
    ) -> None:
        self._init_options = init_options
        self._theme = theme
        self._data = data

    # Set option attributes
    def attr(self, **kwargs) -> Chart:
        pass

    # TODO: Set data here
    def set_data(self, data: DataFrame | dict) -> Chart:
        pass

    def set_option(self, option: dict | ChartOption | BaseOption) -> Chart:
        self._option = option if isinstance(option, dict) else option.to_dict()
        return self

    def to_dict(self) -> dict:
        dataset = (
            df_to_dataset(self._data) if isinstance(self._data, DataFrame) else dict()
        )
        return {
            "initOptions": asdict(self._init_options),
            "option": dataset | self._option,
            "theme": self._theme,
        }
