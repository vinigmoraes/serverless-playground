from jsonschema import Draft7Validator

from books.application.functions.request.validation.error_response import ValidationError
from books.application.functions.request.validation.schemas.create_book_schema import CREATE_BOOK_SCHEMA


class ValidatorRequest:

    @staticmethod
    def validate_create_book_request(json_body):
        validator = Draft7Validator(CREATE_BOOK_SCHEMA)
        errors = sorted(validator.iter_errors(json_body), key=lambda e: e.path)

        validation_errors = []

        for error in errors:
            validation_errors.append(ValidationError(message=error.message, field=error.path))

        return validation_errors
