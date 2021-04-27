import json

from core.domain.book import Book


class GetBookResponse:

    @staticmethod
    def create(book: Book):
        response = {
            "id": str(book.id),
            "title": book.title
        }

        return json.dumps(response)
