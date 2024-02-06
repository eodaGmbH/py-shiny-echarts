from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class InitOptions(object):
    width: int = 600
    height: int = 400


class Chart(object):
    def __init__(
        self, init_options: InitOptions = InitOptions(), theme: str = "dark"
    ) -> None:
        self.init_options = init_options
        self.theme = theme
        self.options = []

    def add(self, option: dict) -> Chart:
        self.options.append(option)
        return self

    def to_dict(self) -> dict:
        return {
            "data": ["Hi", "there"],
            "initOptions": asdict(self.init_options),
            "options": self.options,
            "theme": self.theme,
        }
