import json

from jsonschema import ValidationError

from books.application.application_call import ApplicationCall
from books.application.functions.request.create_book_request import CreateBookRequest
from books.application.functions.request.validation.validation_error_response import ValidationErrorResponse
from books.application.functions.response.create_book_response import CreateBookResponse
from books.domain.usecases.create_book_usecase import CreateBookUseCase


def execute(event, context, use_case: CreateBookUseCase = None):
    use_case = use_case or CreateBookUseCase()

    json_body = json.loads(event["body"])

    try:
        request = CreateBookRequest.from_json(json_body)
    except ValidationError as error:
        return ApplicationCall.respond(
            status_code=400,
            response=ValidationErrorResponse(message=error.message, field=error.path))

    book = use_case.create(request)

    return ApplicationCall.respond(status_code=201, response=CreateBookResponse(book.id, book.title))
