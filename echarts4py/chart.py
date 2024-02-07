from __future__ import annotations

from dataclasses import asdict, dataclass

from pandas import DataFrame


@dataclass
class InitOptions(object):
    width: int = 600
    height: int = 400


class Chart(object):
    """Chart"""

    def __init__(
        self,
        init_options: InitOptions = InitOptions(),
        theme: str = "dark",
        data: DataFrame = None,
    ) -> None:
        self.init_options = init_options
        self.theme = theme
        self.data = data
        self.option = {}

    def add(self, option: dict) -> Chart:
        self.option = option
        return self

    def to_dict(self) -> dict:
        return {
            "data": (
                self.data.to_numpy().tolist()
                if isinstance(self.data, DataFrame)
                else ["Hi", "there"]
            ),
            "initOptions": asdict(self.init_options),
            "option": self.option,
            "theme": self.theme,
        }
