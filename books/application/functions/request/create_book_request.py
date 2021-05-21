from jsonschema import validate

from books.application.functions.request.schemas.create_book_schema import CREATE_BOOK_SCHEMA


class CreateBookRequest:
    title: str

    @classmethod
    def from_json(cls, json_body):
        validate(instance=json_body, schema=CREATE_BOOK_SCHEMA)

        cls.title = json_body["title"]

        return cls
