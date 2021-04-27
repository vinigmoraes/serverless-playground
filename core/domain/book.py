import uuid


class Book:
    id = uuid.uuid4()
    title: str

    def __init__(self, title):
        self.title = title

