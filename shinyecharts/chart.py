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
    """Create a Chart instance"""

    _data: DataFrame = None
    _init_options: dict = None
    _theme: str = None
    _option: dict = None

    def __init__(
        self,
        data: DataFrame = None,
        init_options: InitOptions = InitOptions(),
        theme: str = None,
    ) -> None:
        self._data = data
        self._init_options = asdict(init_options)
        self._theme = theme
        self._option = dict()

    def get_option(self) -> dict:
        """Get option object"""
        return self.to_dict()["option"]

    def configure(self, **kwargs) -> Chart:
        self._init_options.update(kwargs)
        return self

    def attr(self, **kwargs) -> Chart:
        """Set attributes of option object"""
        self._option.update(**kwargs)
        return self

    def set_data(self, data: DataFrame | dict) -> Chart:
        """Set dataset attribute of option object"""
        self._data = data
        return self

    def set_option(self, option: dict | ChartOption | BaseOption) -> Chart:
        """Set option object"""
        self._option = option if isinstance(option, dict) else option.to_dict()
        return self

    def to_dict(self) -> dict:
        dataset = (
            df_to_dataset(self._data) if isinstance(self._data, DataFrame) else dict()
        )
        return {
            "initOptions": self._init_options,
            "option": dataset | self._option,
            "theme": self._theme,
        }
