import json
import uuid


class Book:
    id = uuid.uuid4()
    title: str

    def __init__(self, title):
        self.title = title

    def to_json(self):
        return json.dumps({
            "id": str(self.id),
            "title": self.title
        })
