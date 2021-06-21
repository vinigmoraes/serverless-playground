from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class CreateBookResponse:
    id: str

    def __init__(self, book_id):
        self.id = book_id
