from jsonschema import validate, Draft7Validator

from books.application.functions.request.validation.schemas.create_book_schema import CREATE_BOOK_SCHEMA


class CreateBookRequest:
    title: str
    isbn: str
    hardcover: bool
    book_cover_image: str
    pages: int
    author: str

    @classmethod
    def from_json(cls, json_body):
        cls.title = json_body["title"]
        cls.isbn = json_body["isbn"]
        cls.hardcover = json_body['hardcover']
        cls.book_cover_image = json_body['book_cover_image']
        cls.pages = json_body['pages']
        cls.author = json_body['author']

        return cls
