from dataclasses import dataclass


@dataclass
class ValidationError:
    message: str
    field: str
