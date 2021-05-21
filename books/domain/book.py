import uuid

from books.application.functions.request.create_book_request import CreateBookRequest


class Book:
    id: str
    title: str

    def __init__(self, book_id, title):
        self.id = book_id
        self.title = title

    @staticmethod
    def create(request: CreateBookRequest):
        return Book(
            book_id=uuid.uuid4(),
            title=request.title
        )

    @staticmethod
    def from_json(json):
        return Book(
            book_id=json['id'],
            title=json['title']
        )
