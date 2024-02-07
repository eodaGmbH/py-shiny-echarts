from dataclasses import asdict, dataclass


def snake_to_camel_case(snake_str: str) -> str:
    return snake_str[0].lower() + snake_str.title()[1:].replace("_", "")


@dataclass
class BaseDataClass(object):
    def to_dict(self):
        return asdict(
            self,
            dict_factory=lambda x: {
                snake_to_camel_case(k): v for (k, v) in x if v is not None
            },
        )
