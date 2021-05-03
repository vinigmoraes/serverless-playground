import json


class CreateBookResponse:
    id: str
    title: str

    def __init__(self, book_id, title: str):
        self.id = str(book_id)
        self.title = title

    def to_json(self):
        return json.dumps(self.__dict__)
