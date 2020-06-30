from dataclasses import dataclass, fields


@dataclass(frozen=True)
class ValidBase:
    def __post_init__(self) -> None:
        print(f"{self=}")
        for field in fields(self):
            print(f"{field=}")
            if not isinstance(value := getattr(self, field.name), field.type):
                print(f"{field.type=}")
                object.__setattr__(self, field.name, field.type(value))


@dataclass(frozen=True)
class RequestInterface(ValidBase):
    def to_query(self) -> str:
        return "&".join(
            (f"{attr}={value}" for attr, value in self.__dict__.items())
        )
