import json

from books.core.domain import Book


class GetBookResponse:

    @staticmethod
    def create(book: Book):
        response = {
            "id": str(book.id),
            "title": book.title
        }

        return json.dumps(response)
